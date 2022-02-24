import asyncio
import ctypes as c
from typing import Tuple, Union

import async_timeout

from .. import defines, ftd2xx
from ..ftd2xx import _ft, call_ft
from .transports import FTD2xxTransport


# When asyncio transport and protocol are ready, this class should be removed.
# TODO: Add a warning that this class is on it's way out.
class FTD2XX(ftd2xx.FTD2XX):
    _timeouts: Tuple[int, int] = (0, 0)

    @property
    def timeouts(self):
        return self._timeouts

    @timeouts.setter
    def timeouts(self, timeouts: Tuple[int, int]):
        read, write = timeouts
        super().setTimeouts((1 if read > 0 else 0), write)
        self._timeouts = (max(timeouts[0], 0), max(timeouts[1], 0))

    # TODO: may be this should renamed to read_async
    async def read(self, nchars: int, raw=True, exc=False):  # type: ignore
        timeout, _ = self.timeouts
        timeout = timeout / 1000.0 if timeout else None

        cm = async_timeout.timeout(timeout)
        try:
            async with cm:
                while self.getQueueStatus() < nchars:
                    await asyncio.sleep(1e-3)
        finally:
            if exc and cm.expired:
                raise asyncio.TimeoutError

            return super().read(nchars, raw)

    def write(self, data, exc=False):
        length = super().write(data)
        if exc:
            if length < len(data):
                raise asyncio.TimeoutError
        return length

    def setTimeouts(self, read, write):
        self.timeouts = read, write


# TODO: Remove when transports are stable.
def open(dev=0):
    """Open a handle to a usb device by index and return an FTD2XX instance for
    it"""
    h = _ft.FT_HANDLE()
    call_ft(_ft.FT_Open, dev, c.byref(h))
    return FTD2XX(h)


# TODO: Remove when transports are stable.
def openEx(id_str, flags=defines.OPEN_BY_SERIAL_NUMBER):
    """Open a handle to a usb device by serial number(default), description or
    location(Windows only) depending on value of flags and return an FTD2XX
    instance for it"""
    h = _ft.FT_HANDLE()
    call_ft(_ft.FT_OpenEx, id_str, _ft.DWORD(flags), c.byref(h))
    return FTD2XX(h)


#
# Parts of this code are inspired by or directly copied from the work of the
# pyserial team (pyserial-asyncio) which is under BSD3 license.
# Project Homepage: https://github.com/pyserial/pyserial-asyncio
#
async def create_ftd2xx_connection(
    loop,
    protocol_factory,
    dev_id: Union[int, bytes] = 0,
    flags: defines.OpenExFlags = defines.OPEN_BY_SERIAL_NUMBER,
):
    """Create a connection to a new ftd2xx instance.
    This function is a coroutine which will try to establish the
    connection.
    The chronological order of the operation is:
    1. protocol_factory is called without arguments and must return
       a protocol instance.
    2. The protocol instance is tied to the transport
    3. This coroutine returns successfully with a (transport,
       protocol) pair.
    4. The connection_made() method of the protocol
       will be called at some point by the event loop.
    Note:  protocol_factory can be any kind of callable, not
    necessarily a class. For example, if you want to use a pre-created
    protocol instance, you can pass lambda: my_protocol.
    Any additional arguments will be forwarded to open() or openEx() to create
    an FTD2XX instance.
    """

    async def create_tp_pair():
        if isinstance(dev_id, int) and flags != defines.OPEN_BY_LOCATION:
            ftd2xx_instance = ftd2xx.open(dev_id)
        else:
            ftd2xx_instance = ftd2xx.openEx(dev_id, defines.OpenExFlags(flags))

        protocol = protocol_factory()

        return FTD2xxTransport(loop, protocol, ftd2xx_instance), protocol

    return await create_tp_pair()


async def open_ftd2xx_connection(*, loop=None, limit=None, **kwargs):
    """A wrapper for create_ftd2xx_connection() returning a (reader,
    writer) pair.
    The reader returned is a StreamReader instance; the writer is a
    StreamWriter instance.
    The arguments are all the usual arguments to open(). Additional
    optional keyword arguments are loop (to set the event loop instance
    to use) and limit (to set the buffer limit passed to the
    StreamReader.
    This function is a coroutine.
    """
    # if loop is None:
    #     loop = asyncio.get_event_loop()
    # if limit is None:
    #     limit = asyncio.streams._DEFAULT_LIMIT
    # reader = asyncio.StreamReader(limit=limit, loop=loop)
    # protocol = asyncio.StreamReaderProtocol(reader, loop=loop)
    # transport, _ = await create_serial_connection(
    #     loop=loop, protocol_factory=lambda: protocol, **kwargs
    # )
    # writer = asyncio.StreamWriter(transport, protocol, reader, loop)
    # return reader, writer
    raise NotImplementedError
