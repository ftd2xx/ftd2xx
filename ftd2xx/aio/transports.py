#
# Parts of this code are inspired by or directly copied from the work of the
# pyserial team (asyncio-serial) which is under BSD3 license.
# Project Homepage: https://github.com/pyserial/pyserial-asyncio
#
"""Asyncio transports for FTDI D2XX devices."""
from abc import abstractmethod
import asyncio
from ..ftd2xx import DeviceError


class FTD2xxBaseTransport(asyncio.BaseTransport):
    """Base class for FTDI D2XX transports."""

    def __init__(self, loop, protocol, ftd2xx_instance):
        super().__init__()
        self._loop = loop
        self._protocol = protocol
        self._ftd2xx = ftd2xx_instance
        self._closing = False
        self._poll_wait_time = 0.0005

        self._ftd2xx.setTimeouts(1, 1)  # Non-blocking
        loop.call_soon(protocol.connection_made, self)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}({self.loop}, {self._protocol}, {self.ftd2xx})"
        )

    @property
    def loop(self):
        """The asyncio event loop used by this FTD2xxTransport."""
        return self._loop

    @property
    def ftd2xx(self):
        """The underlying FTD2XX instance.
        Equivalent to get_extra_info("ftd2xx")
        """
        return self._ftd2xx

    def get_extra_info(self, name, default=None):
        """Get optional transport information.
        Currently only "ftd2xx" is available.
        """
        if name == "ftd2xx":
            return self._ftd2xx
        return default

    def is_closing(self):
        """Return True if the transport is closing or closed."""
        return self._closing

    def close(self):
        """Close the transport gracefully.
        Any buffered data will be written asynchronously. No more data
        will be received and further writes will be silently ignored.
        After all buffered data is flushed, the protocol's
        connection_lost() method will be called with None as its
        argument.
        """
        if not self._closing:
            self._close(None)

    # TODO: Should implement??
    # def set_protocol(self, protocol):
    #     raise NotImplementedError
    #
    # def get_protocol(self):
    #     raise NotImplementedError

    @abstractmethod
    def _shutdown(self):
        """Minimal cleanup when immediate shutdown is needed."""

    @abstractmethod
    def _graceful_shutdown(self) -> bool:
        """Cleanup when graceful shutdown is desired. Returns True when cleanup
        is complete, otherwise False."""
        return True

    def _fatal_error(self, exc, message="Fatal error on ftd2xx transport"):
        """Report a fatal error to the event-loop and abort the transport."""
        self._loop.call_exception_handler(
            {
                "message": message,
                "exception": exc,
                "transport": self,
                "protocol": self._protocol,
            }
        )
        self._abort(exc)

    def _abort(self, exc):
        """Close the transport immediately.
        Pending operations will not be given opportunity to complete,
        and buffered data will be lost. No more data will be received
        and further writes will be ignored.  The protocol's
        connection_lost() method will eventually be called with the
        passed exception.
        """
        self._closing = True
        self._shutdown()
        self._loop.call_soon(self._call_connection_lost, exc)

    def _close(self, exc=None):
        """Close the transport gracefully.
        If the write buffer is already empty, writing will be
        stopped immediately and a call to the protocol's
        connection_lost() method scheduled.
        If the write buffer is not already empty, the
        asynchronous writing will continue, and the _write_ready
        method will call this _close method again when the
        buffer has been flushed completely.
        """
        self._closing = True
        if self._graceful_shutdown():
            self._loop.call_soon(self._call_connection_lost, exc)

    @abstractmethod
    def _call_connection_lost(self, exc):
        """Close the connection.
        Informs the protocol through connection_lost() and clears
        pending buffers and closes the connection.
        """
        assert self._closing

        # Ignore errors from hot-unplug
        try:
            self._ftd2xx.purge()
        except DeviceError:
            pass

        try:
            self._protocol.connection_lost(exc)
        finally:
            self._post_connection_lost()

    def _post_connection_lost(self):
        self._ftd2xx.close()
        self._ftd2xx = None
        self._protocol = None
        self._loop = None


class FTD2xxReadTransport(FTD2xxBaseTransport, asyncio.ReadTransport):
    """FTDI D2XX read-only transport."""

    def __init__(self, loop, protocol_factory, ftd2xx_instance):
        super().__init__(loop, protocol_factory, ftd2xx_instance)
        self._max_read_size = 1024
        self._has_reader = False
        self._modem = 0  # TODO
        loop.call_soon(self._ensure_reader)

    def _read_ready(self):
        try:
            data = self._ftd2xx.read(self._max_read_size)
        except DeviceError as exc:
            self._close(exc=exc)
        else:
            if data:
                self._protocol.data_received(data)

    def pause_reading(self):
        """Pause the receiving end of the transport.
        No data will be passed to the protocol’s data_received() method
        until resume_reading() is called.
        """
        self._remove_reader()

    def resume_reading(self):
        """Resume the receiving end of the transport.
        Incoming data will be passed to the protocol's data_received()
        method until pause_reading() is called.
        """
        self._ensure_reader()

    def _shutdown(self):
        self._remove_reader()
        super()._shutdown()

    def _graceful_shutdown(self) -> bool:
        if super()._graceful_shutdown():
            self._remove_reader()
            return True
        return False

    def _call_connection_lost(self, exc):
        assert not self._has_reader
        super()._call_connection_lost(exc)

    async def _poll_read(self):
        # TODO: Use events
        while True:
            try:
                if self._ftd2xx.getQueueStatus():
                    self._read_ready()
                await asyncio.sleep(self._poll_wait_time)
            except DeviceError as exc:
                self._fatal_error(exc, "Fatal write error on ftd2xx transport")

    async def _poll_modem(self):
        while True:
            try:
                modem = self._ftd2xx.getModemStatus()
                if self._modem != modem:
                    print(modem)
                    self._modem = modem
                await asyncio.sleep(self._poll_wait_time)
            except DeviceError as exc:
                self._fatal_error(exc, "Fatal write error on ftd2xx transport")

    def _ensure_reader(self):
        if not self._has_reader and not self._closing:
            self._has_reader = self._loop.create_task(self._poll_read())
            self._loop.create_task(self._poll_modem())  # TODO

    def _remove_reader(self):
        if self._has_reader:
            self._has_reader.cancel()
        self._has_reader = False


class FTD2xxWriteTransport(FTD2xxBaseTransport, asyncio.WriteTransport):
    """FTDI D2XX write-only transport."""

    def __init__(self, loop, protocol_factory, ftd2xx_instance):
        super().__init__(loop, protocol_factory, ftd2xx_instance)
        self._write_buffer = []
        self._protocol_paused = False
        self._has_writer = False
        self._max_out_waiting = 1024
        self._set_write_buffer_limits()

    def set_write_buffer_limits(self, high=None, low=None):
        """Set the high- and low-water limits for write flow control.
        These two values control when the protocol’s
        pause_writing()and resume_writing() methods are called. If
        specified, the low-water limit must be less than or equal to
        the high-water limit. Neither high nor low can be negative.
        """
        self._set_write_buffer_limits(high=high, low=low)
        self._maybe_pause_protocol()

    def get_write_buffer_size(self):
        """The number of bytes in the write buffer.
        This buffer is unbounded, so the result may be larger than the
        the high water mark.
        """
        return sum(map(len, self._write_buffer))

    def write(self, data):
        """Write some data to the transport.
        This method does not block; it buffers the data and arranges
        for it to be sent out asynchronously.  Writes made after the
        transport has been closed will be ignored."""
        if self._closing:
            return

        if self.get_write_buffer_size() == 0:
            self._write_buffer.append(data)
            self._ensure_writer()
        else:
            self._write_buffer.append(data)

        self._maybe_pause_protocol()

    def write_eof(self):
        exc = NotImplementedError("FTD2XX connections do not support end-of-file")
        raise exc

    def can_write_eof(self):
        """Serial ports do not support the concept of end-of-file.
        Always returns False.
        """
        return False

    def abort(self):
        """Close the transport immediately.
        Pending operations will not be given opportunity to complete,
        and buffered data will be lost. No more data will be received
        and further writes will be ignored.  The protocol's
        connection_lost() method will eventually be called.
        """
        self._abort(None)

    def flush(self):
        """clears output buffer and stops any more data being written"""
        self._remove_writer()
        self._write_buffer.clear()
        self._maybe_resume_protocol()

    def _flushed(self):
        """True if the write buffer is empty, otherwise False."""
        return self.get_write_buffer_size() == 0

    def _maybe_pause_protocol(self):
        """To be called whenever the write-buffer size increases.
        Tests the current write-buffer size against the high water
        mark configured for this transport. If the high water mark is
        exceeded, the protocol is instructed to pause_writing().
        """
        if self.get_write_buffer_size() <= self._high_water:
            return
        if not self._protocol_paused:
            self._protocol_paused = True
            try:
                self._protocol.pause_writing()
            except Exception as exc:  # pylint: disable=broad-except
                self._loop.call_exception_handler(
                    {
                        "message": "protocol.pause_writing() failed",
                        "exception": exc,
                        "transport": self,
                        "protocol": self._protocol,
                    }
                )

    def _maybe_resume_protocol(self):
        """To be called whenever the write-buffer size decreases.
        Tests the current write-buffer size against the low water
        mark configured for this transport. If the write-buffer
        size is below the low water mark, the protocol is
        instructed that is can resume_writing().
        """
        if self._protocol_paused and self.get_write_buffer_size() <= self._low_water:
            self._protocol_paused = False
            try:
                self._protocol.resume_writing()
            except Exception as exc:  # pylint: disable=broad-except
                self._loop.call_exception_handler(
                    {
                        "message": "protocol.resume_writing() failed",
                        "exception": exc,
                        "transport": self,
                        "protocol": self._protocol,
                    }
                )

    def _write_ready(self):
        """Asynchronously write buffered data.
        This method is called back asynchronously as a writer
        registered with the asyncio event-loop against the
        underlying file descriptor for the serial port.
        Should the write-buffer become empty if this method
        is invoked while the transport is closing, the protocol's
        connection_lost() method will be called with None as its
        argument.
        """
        data = b"".join(self._write_buffer)
        assert data, "Write buffer should not be empty"

        self._write_buffer.clear()

        try:
            nchars = self._ftd2xx.write(data)
        except (BlockingIOError, InterruptedError):
            self._write_buffer.append(data)
        except DeviceError as exc:
            self._fatal_error(exc, "Fatal write error on ftd2xx transport")
        else:
            if nchars == len(data):
                assert self._flushed()
                self._remove_writer()
                self._maybe_resume_protocol()  # May cause further writes
                # _write_ready may have been invoked by the event loop
                # after the transport was closed, as part of the ongoing
                # process of flushing buffered data. If the buffer
                # is now empty, we can close the connection
                if self._closing and self._flushed():
                    self._close()
                return

            assert 0 <= nchars < len(data)
            data = data[nchars:]
            self._write_buffer.append(data)  # Try again later
            self._maybe_resume_protocol()
            assert self._has_writer

    def _set_write_buffer_limits(self, high=None, low=None):
        """Ensure consistent write-buffer limits."""
        if high is None:
            high = 64 * 1024 if low is None else 4 * low
        if low is None:
            low = high // 4
        if not high >= low >= 0:
            raise ValueError(f"high ({high}) must be >= low ({low}) must be >= 0")
        self._high_water = high
        self._low_water = low

    def _shutdown(self):
        super()._shutdown()
        self._remove_writer()

    def _graceful_shutdown(self) -> bool:
        if super()._graceful_shutdown():
            if self._flushed():
                self._remove_writer()
                return True
        return False

    def _call_connection_lost(self, exc):
        assert not self._has_writer
        super()._call_connection_lost(exc)

    def _post_connection_lost(self):
        self._write_buffer.clear()
        super()._post_connection_lost()

    def _poll_write(self):
        if self._has_writer and not self._closing:
            self._has_writer = self._loop.call_later(
                self._poll_wait_time, self._poll_write
            )
            # Check tx queue
            if self._ftd2xx.getStatus()[1] < self._max_out_waiting:
                self._write_ready()

    def _ensure_writer(self):
        if not self._has_writer and not self._closing:
            self._has_writer = self._loop.call_soon(self._poll_write)

    def _remove_writer(self):
        if self._has_writer:
            self._has_writer.cancel()
        self._has_writer = False


class FTD2xxTransport(FTD2xxReadTransport, FTD2xxWriteTransport):
    """FTDI D2XX bidirectional transport."""
