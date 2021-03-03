import asyncio
import ctypes as c
from .defines import *
from .ftd2xx import *
from .ftd2xx import _ft


class FTD2XX(ftd2xx.FTD2XX):
    timeouts = None, None
    
    async def read(self, nchars: int, raw=True):
        async def bytes_ready(n):
            while not self.getQueueStatus() >= nchars:
                await asyncio.sleep(1e-3)  # Non-zero to save CPU (specific to my application, maybe there is a better general approach)

        try:
            await asyncio.wait_for(bytes_ready(nchars), timeout=self.timeouts[0])
        finally:
            return super().read(nchars, raw)
    
    def setTimeouts(self, read, write):
        super().setTimeouts(
            (read if not read > 0 else 1),
            (write if not write > 0 else 1)
        )
        self.timeouts = (
            (None if not read > 0 else (read - 1) / 1000.0),
            (None if not write > 0 else (write - 1) / 1000.0)
        )

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
