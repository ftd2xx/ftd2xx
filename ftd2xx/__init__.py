"""
Control FTDI USB chips.

Use :any:`ftd2xx.open` or :any:`ftd2xx.openEx`.
:example:
    with open(0) as device:
        device.write(b"Hello World!")
"""

import sys

try:
    from _version import (
        __version__ as __version__,
        __version_tuple__ as __version_tuple__,
    )
except ImportError:
    __version__ = "unknown"
    __version_tuple__ = (0, 0, 0, "unknown", "unknown")

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
