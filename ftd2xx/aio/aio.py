import asyncio
import ctypes as c
from typing import Tuple
from .. import defines
from .. import ftd2xx
from ..ftd2xx import _ft, call_ft


class FTD2XX(ftd2xx.FTD2XX):
    _timeouts = 0, 0

    @property
    def timeouts(self):
        return self._timeouts

    @timeouts.setter
    def timeouts(self, timeouts: Tuple[float, float]):
        super().setTimeouts(*[1 if t > 0 else 0 for t in timeouts])
        self._timeouts = [t if t > 0 else 0 for t in timeouts]

    async def read(self, nchars: int, raw=True, exc=False):
        async def bytes_ready(n):
            while self.getQueueStatus() < nchars:
                await asyncio.sleep(
                    1e-3
                )  # Non-zero to save CPU (maybe there is a better approach)

        try:
            timeout, _ = self.timeouts
            timeout = (timeout - 1) / 1000.0 if timeout else None
            if exc:
                timeout += 1e-3
            await asyncio.wait_for(bytes_ready(nchars), timeout=timeout)
        except asyncio.TimeoutError:
            if exc:
                raise
        finally:
            return super().read(nchars, raw)

    def write(self, data, exc=False):
        length = super().write(data)
        if exc:
            if length < len(data):
                raise asyncio.TimeoutError
        return length

    def setTimeouts(self, read, write):
        self.timeouts = read, write


def open(dev=0):
    """Open a handle to a usb device by index and return an FTD2XX instance for
    it"""
    h = _ft.FT_HANDLE()
    call_ft(_ft.FT_Open, dev, c.byref(h))
    return FTD2XX(h)


def openEx(id_str, flags=defines.OPEN_BY_SERIAL_NUMBER):
    """Open a handle to a usb device by serial number(default), description or
    location(Windows only) depending on value of flags and return an FTD2XX
    instance for it"""
    h = _ft.FT_HANDLE()
    call_ft(_ft.FT_OpenEx, id_str, _ft.DWORD(flags), c.byref(h))
    return FTD2XX(h)
