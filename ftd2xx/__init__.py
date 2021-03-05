"""
Control FTDI USB chips.

Open a handle using ftd2xx.open or ftd2xx.openEx and use the methods
on the object thus returned.

There are a few convenience functions too
"""
from __future__ import absolute_import
import sys

from .ftd2xx import *
from . import aio


__all__ = [
    "call_ft",
    "listDevices",
    "getLibraryVersion",
    "createDeviceInfoList",
    "getDeviceInfoDetail",
    "open",
    "openEx",
    "FTD2XX",
    "DeviceError",
    "ft_program_data",
    "aio",
]
if sys.platform == "win32":
    __all__ += ["w32CreateFile"]
else:
    __all__ += ["getVIDPID", "setVIDPID"]
