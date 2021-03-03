import asyncio
import ctypes as c
from ..defines import *
from ..ftd2xx import *
from ..ftd2xx import _ft


class FTD2XX(FTD2XX):
    _timeouts = None, None
    
    @property
    def timeouts(self): return self._timeouts
    
    @timeouts.setter
    def timeouts(self, timeouts: tuple):
        super().setTimeouts(*[1 if t > 0 else 0 for t in timeouts])
        self._timeouts = tuple([t if t > 0 else 0 for t in timeouts])
    
    async def read(self, nchars: int, raw=True):
        async def bytes_ready(n):
            while self.getQueueStatus() < nchars:
                await asyncio.sleep(1e-3)  # Non-zero to save CPU (specific to my application, maybe there is a better general approach)

        try:
            timeout, _ = self.timeouts
            timeout = (timeout - 1) / 1000.0 if timeout else None
            await asyncio.wait_for(bytes_ready(nchars), timeout=timeout)
        finally:
            return super().read(nchars, raw)
    
    def setTimeouts(self, read, write):
        self.timeouts = read, write

def open(dev=0):
    """Open a handle to a usb device by index and return an FTD2XX instance for
    it"""
    h = _ft.FT_HANDLE()
    call_ft(_ft.FT_Open, dev, c.byref(h))
    return FTD2XX(h)

def openEx(id_str, flags=OPEN_BY_SERIAL_NUMBER):
    """Open a handle to a usb device by serial number(default), description or
    location(Windows only) depending on value of flags and return an FTD2XX
    instance for it"""
    h = _ft.FT_HANDLE()
    call_ft(_ft.FT_OpenEx, id_str, _ft.DWORD(flags), c.byref(h))
    return FTD2XX(h)
