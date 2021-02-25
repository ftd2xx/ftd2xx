import asyncio
import ctypes as c
from .defines import *
from .ftd2xx import *
from .ftd2xx import BaseFTD2XX, _ft


class FTD2XX(BaseFTD2XX):
  async def read(self, nchars: int, raw=True):
    while not self.getQueueStatus() >= nchars:
      await asyncio.sleep(1e-3)  # Non-zero to save CPU (specific to my application, maybe there is a better general approach)
    return self._read(nchars, raw)

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
