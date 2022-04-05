"""
Control FTDI USB chips.

Open a handle using ftd2xx.open or ftd2xx.openEx and use the methods
on the object thus returned.

There are a few convenience functions too
"""
from __future__ import absolute_import

import sys

from .ftd2xx import (
    FTD2XX,
    DeviceError,
    call_ft,
    createDeviceInfoList,
    ft_program_data,
    getDeviceInfoDetail,
    getLibraryVersion,
    listDevices,
    open,
    openEx,
)

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
]
if sys.platform == "win32":
    from .ftd2xx import w32CreateFile

    __all__ += ["w32CreateFile"]
else:
    from .ftd2xx import getVIDPID, setVIDPID

    __all__ += ["getVIDPID", "setVIDPID"]
