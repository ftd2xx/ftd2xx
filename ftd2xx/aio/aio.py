import asyncio
import ctypes as c
from typing import Tuple

import async_timeout

from .. import defines, ftd2xx
from ..ftd2xx import _ft, call_ft


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
