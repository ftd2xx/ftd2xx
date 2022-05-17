"""FTD2xx library functions for Windows."""
from typing import Union, Callable
import os
import sys
from ctypes import WinDLL, CDLL
from . import api_classic as classic
from . import api_eeprom as eeprom
from . import api_ext as ext
from . import api_win32 as w32

if sys.platform == "win32":
    # If you need non-standard DLL directory, set FTD2XX_DLL_DIR to absoluate path to dll
    extra_dll_dir = os.environ.get("FTD2XX_DLL_DIR")
    if extra_dll_dir:
        if sys.version_info >= (3, 8):
            os.add_dll_directory(extra_dll_dir)
        else:
            os.environ.setdefault("PATH", "")
            os.environ["PATH"] += os.pathsep + extra_dll_dir
    try:
        LIB_FTD2XX = WinDLL("ftd2xx64.dll")
    except OSError:  # 32-bit, or 64-bit library with plain name
        try:
            LIB_FTD2XX = WinDLL("ftd2xx.dll")
        except OSError as e:
            if e.winerror == 126:
                error_message = (
                    e.args[1]
                    + "Unable to find D2XX DLL. Please make sure that the directory "
                    "containing your DLL is in one (or both) environment variables: 'PATH', "
                    "'FTD2XX_DLL_DIR'. Also, you must use 'ftd2xx.dll' or 'ftd2xx64.dll' as the "
                    "filename."
                )
                e.args = (e.args[0], error_message) + e.args[2:]
            raise e
elif sys.platform.startswith("linux"):
    LIB_FTD2XX = CDLL("libftd2xx.so")
elif sys.platform == "darwin":
    LIB_FTD2XX = CDLL("/usr/local/lib/libftd2xx.dylib")
else:
    raise Exception("Unknown platform")


def dll_func(lib: Union[WinDLL, CDLL], proto: Callable):
    """Populates return and arg types for DLL function using annotations.

    Args:
        lib: A ctypes CDLL/WinDLL object.
        proto: A dummy python function with annotations.

    Returns:
        Function pointer.
    """
    try:
        f_ptr = getattr(lib, proto.__name__)
    except AttributeError:

        def unsupported(*args):
            raise Exception("Function is not supported by this driver!")

        return unsupported

    f_ptr.argtypes = [
        argtype
        for argname, argtype in proto.__annotations__.items()
        if argname != "return"
    ]
    try:
        f_ptr.restype = proto.__annotations__["return"]
    except KeyError:
        pass
    f_ptr.__doc__ = proto.__doc__

    return f_ptr


# CLASSIC
FT_SetVIDPID = dll_func(LIB_FTD2XX, classic.FT_SetVIDPID)
FT_GetVIDPID = dll_func(LIB_FTD2XX, classic.FT_GetVIDPID)
FT_CreateDeviceInfoList = dll_func(LIB_FTD2XX, classic.FT_CreateDeviceInfoList)
FT_GetDeviceInfoList = dll_func(LIB_FTD2XX, classic.FT_GetDeviceInfoList)
FT_GetDeviceInfoDetail = dll_func(LIB_FTD2XX, classic.FT_GetDeviceInfoDetail)
FT_ListDevices = dll_func(LIB_FTD2XX, classic.FT_ListDevices)
FT_Open = dll_func(LIB_FTD2XX, classic.FT_Open)
FT_OpenEx = dll_func(LIB_FTD2XX, classic.FT_OpenEx)
FT_Close = dll_func(LIB_FTD2XX, classic.FT_Close)
FT_Read = dll_func(LIB_FTD2XX, classic.FT_Read)
FT_Write = dll_func(LIB_FTD2XX, classic.FT_Write)
FT_SetBaudRate = dll_func(LIB_FTD2XX, classic.FT_SetBaudRate)
FT_SetDivisor = dll_func(LIB_FTD2XX, classic.FT_SetDivisor)
FT_SetDataCharacteristics = dll_func(LIB_FTD2XX, classic.FT_SetDataCharacteristics)
FT_SetTimeouts = dll_func(LIB_FTD2XX, classic.FT_SetTimeouts)
FT_SetFlowControl = dll_func(LIB_FTD2XX, classic.FT_SetFlowControl)
FT_SetDtr = dll_func(LIB_FTD2XX, classic.FT_SetDtr)
FT_ClrDtr = dll_func(LIB_FTD2XX, classic.FT_ClrDtr)
FT_SetRts = dll_func(LIB_FTD2XX, classic.FT_SetRts)
FT_ClrRts = dll_func(LIB_FTD2XX, classic.FT_ClrRts)
FT_GetModemStatus = dll_func(LIB_FTD2XX, classic.FT_GetModemStatus)
FT_GetQueueStatus = dll_func(LIB_FTD2XX, classic.FT_GetQueueStatus)
FT_GetDeviceInfo = dll_func(LIB_FTD2XX, classic.FT_GetDeviceInfo)
FT_GetDriverVersion = dll_func(LIB_FTD2XX, classic.FT_GetDriverVersion)
FT_GetLibraryVersion = dll_func(LIB_FTD2XX, classic.FT_GetLibraryVersion)
FT_GetComPortNumber = dll_func(LIB_FTD2XX, classic.FT_GetComPortNumber)
FT_GetStatus = dll_func(LIB_FTD2XX, classic.FT_GetStatus)
FT_SetEventNotification = dll_func(LIB_FTD2XX, classic.FT_SetEventNotification)
FT_SetChars = dll_func(LIB_FTD2XX, classic.FT_SetChars)
FT_SetBreakOn = dll_func(LIB_FTD2XX, classic.FT_SetBreakOn)
FT_SetBreakOff = dll_func(LIB_FTD2XX, classic.FT_SetBreakOff)
FT_Purge = dll_func(LIB_FTD2XX, classic.FT_Purge)
FT_ResetDevice = dll_func(LIB_FTD2XX, classic.FT_ResetDevice)
FT_ResetPort = dll_func(LIB_FTD2XX, classic.FT_ResetPort)
FT_CyclePort = dll_func(LIB_FTD2XX, classic.FT_CyclePort)
FT_Rescan = dll_func(LIB_FTD2XX, classic.FT_Rescan)
FT_Reload = dll_func(LIB_FTD2XX, classic.FT_Reload)
FT_SetResetPipeRetryCount = dll_func(LIB_FTD2XX, classic.FT_SetResetPipeRetryCount)
FT_StopInTask = dll_func(LIB_FTD2XX, classic.FT_StopInTask)
FT_RestartInTask = dll_func(LIB_FTD2XX, classic.FT_RestartInTask)
FT_SetDeadmanTimeout = dll_func(LIB_FTD2XX, classic.FT_SetDeadmanTimeout)
FT_IoCtl = dll_func(LIB_FTD2XX, classic.FT_IoCtl)
FT_SetWaitMask = dll_func(LIB_FTD2XX, classic.FT_SetWaitMask)
FT_WaitOnMask = dll_func(LIB_FTD2XX, classic.FT_WaitOnMask)
FT_GetEventStatus = dll_func(LIB_FTD2XX, classic.FT_GetEventStatus)

# EEPROM
FT_ReadEE = dll_func(LIB_FTD2XX, eeprom.FT_ReadEE)
FT_WriteEE = dll_func(LIB_FTD2XX, eeprom.FT_WriteEE)
FT_EraseEE = dll_func(LIB_FTD2XX, eeprom.FT_EraseEE)
FT_EE_Read = dll_func(LIB_FTD2XX, eeprom.FT_EE_Read)
FT_EE_ReadEx = dll_func(LIB_FTD2XX, eeprom.FT_EE_ReadEx)
FT_EE_Program = dll_func(LIB_FTD2XX, eeprom.FT_EE_Program)
FT_EE_ProgramEx = dll_func(LIB_FTD2XX, eeprom.FT_EE_ProgramEx)
FT_EE_UASize = dll_func(LIB_FTD2XX, eeprom.FT_EE_UASize)
FT_EE_UARead = dll_func(LIB_FTD2XX, eeprom.FT_EE_UARead)
FT_EE_UAWrite = dll_func(LIB_FTD2XX, eeprom.FT_EE_UAWrite)
FT_EEPROM_Read = dll_func(LIB_FTD2XX, eeprom.FT_EEPROM_Read)
FT_EEPROM_Program = dll_func(LIB_FTD2XX, eeprom.FT_EEPROM_Program)

# EXTENDED
FT_SetLatencyTimer = dll_func(LIB_FTD2XX, ext.FT_SetLatencyTimer)
FT_GetLatencyTimer = dll_func(LIB_FTD2XX, ext.FT_GetLatencyTimer)
FT_SetBitMode = dll_func(LIB_FTD2XX, ext.FT_SetBitMode)
FT_GetBitMode = dll_func(LIB_FTD2XX, ext.FT_GetBitMode)
FT_SetUSBParameters = dll_func(LIB_FTD2XX, ext.FT_SetUSBParameters)

# WIN32
FT_W32_CreateFile = dll_func(LIB_FTD2XX, w32.FT_W32_CreateFile)
