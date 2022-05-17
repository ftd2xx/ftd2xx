"""FT-Win32 API"""
from ctypes import POINTER, CFUNCTYPE
from .typedefs import (
    FT_HANDLE,
    FT_STATUS,
    FT_DEVICE,
    LPOVERLAPPED,
    LPSECURITY_ATTRIBUTES,
    ft_program_data,
    PFT_PROGRAM_DATA,
    ft_eeprom_header,
    ft_eeprom_x_series,
    LPFTCOMSTAT,
    LPFTDCB,
    FTTIMEOUTS,
    FT_DEVICE_LIST_INFO_NODE,
    # VOID,
    BOOL,
    BYTE,
    UCHAR,
    USHORT,
    WORD,
    DWORD,
    INT,
    ULONG,
    # ULONGLONG,
    STRING,
    HANDLE,
    PVOID,
    PCHAR,
    PUCHAR,
    PULONG,
    LPVOID,
    LPCSTR,
    # LPTSTR,
    LPWORD,
    LPDWORD,
    LPLONG,
)


# values for unnamed enumeration
PFT_EVENT_HANDLER = CFUNCTYPE(None, ULONG, ULONG)


# pylint: disable=C0103
# pylint: disable=unused-argument
# pylint: disable=too-many-arguments


def FT_W32_CreateFile(
    lpszName: LPCSTR,
    dwAccess: DWORD,
    dwShareMode: DWORD,
    lpSecurityAttributes: LPSECURITY_ATTRIBUTES,
    dwCreate: DWORD,
    dwAttrsAndFlags: DWORD,
    hTemplate: HANDLE,
) -> FT_HANDLE:
    """Opens the specified device and return a handle which will be used for subsequent accesses.
        The device can be specified by its serial number, device description, or location.

    Args:
        lpszName (LPCSTR): Meaning depends on the value of dwAttrsAndFlags. Can be a pointer to a
            null terminated string that contains the description or serial number of the device, or
            can be the location of the device. These values can be obtained from the
            FT_CreateDeviceInfoList, FT_GetDeviceInfoDetail or FT_ListDevices functions.
        dwAccess (DWORD): Type of access to the device. Access can be GENERIC_READ, GENERIC_WRITE
            or both. Ignored in Linux.
        dwShareMode (DWORD): How the device is shared. This value must be set to 0.
        lpSecurityAttributes (LPSECURITY_ATTRIBUTES): This parameter has no effect and should be
            set to NULL.
        dwCreate (DWORD): This parameter must be set to OPEN_EXISTING. Ignored in Linux.
        dwAttrsAndFlags (DWORD): File attributes and flags. This parameter is a combination of
            FILE_ATTRIBUTE_NORMAL, FILE_FLAG_OVERLAPPED if overlapped I/O is used,
            FT_OPEN_BY_SERIAL_NUMBER if lpszName is the device’s serial number, and
            FT_OPEN_BY_DESCRIPTION if lpszName is the device’s description.
        hTemplate (HANDLE): This parameter must be NULL.

    Returns:
        If the function is successful, the return value is a handle.
        If the function is unsuccessful, the return value is the Win32 error code
        INVALID_HANDLE_VALUE.
    """


# # ftd2xx.h 643
# FT_W32_CloseHandle = LIB_FTD2XX.FT_W32_CloseHandle
# FT_W32_CloseHandle.restype = BOOL
# # FT_W32_CloseHandle(ftHandle)
# FT_W32_CloseHandle.argtypes = [FT_HANDLE]
# FT_W32_CloseHandle.__doc__ = """BOOL FT_W32_CloseHandle(FT_HANDLE ftHandle)
# ftd2xx.h:643"""
# # ftd2xx.h 652
# FT_W32_ReadFile = LIB_FTD2XX.FT_W32_ReadFile
# FT_W32_ReadFile.restype = BOOL
# # FT_W32_ReadFile(ftHandle, lpBuffer, nBufferSize, lpBytesReturned, lpOverlapped)
# FT_W32_ReadFile.argtypes = [FT_HANDLE, LPVOID, DWORD, LPDWORD, LPOVERLAPPED]
# FT_W32_ReadFile.__doc__ = """BOOL FT_W32_ReadFile(FT_HANDLE ftHandle, LPVOID lpBuffer, DWORD nBufferSize, LPDWORD lpBytesReturned, LPOVERLAPPED lpOverlapped)
# ftd2xx.h:652"""
# # ftd2xx.h 661
# FT_W32_WriteFile = LIB_FTD2XX.FT_W32_WriteFile
# FT_W32_WriteFile.restype = BOOL
# # FT_W32_WriteFile(ftHandle, lpBuffer, nBufferSize, lpBytesWritten, lpOverlapped)
# FT_W32_WriteFile.argtypes = [FT_HANDLE, LPVOID, DWORD, LPDWORD, LPOVERLAPPED]
# FT_W32_WriteFile.__doc__ = """BOOL FT_W32_WriteFile(FT_HANDLE ftHandle, LPVOID lpBuffer, DWORD nBufferSize, LPDWORD lpBytesWritten, LPOVERLAPPED lpOverlapped)
# ftd2xx.h:661"""
# # ftd2xx.h 666
# FT_W32_GetLastError = LIB_FTD2XX.FT_W32_GetLastError
# FT_W32_GetLastError.restype = DWORD
# # FT_W32_GetLastError(ftHandle)
# FT_W32_GetLastError.argtypes = [FT_HANDLE]
# FT_W32_GetLastError.__doc__ = """DWORD FT_W32_GetLastError(FT_HANDLE ftHandle)
# ftd2xx.h:666"""
# # ftd2xx.h 674
# FT_W32_GetOverlappedResult = LIB_FTD2XX.FT_W32_GetOverlappedResult
# FT_W32_GetOverlappedResult.restype = BOOL
# # FT_W32_GetOverlappedResult(ftHandle, lpOverlapped, lpdwBytesTransferred, bWait)
# FT_W32_GetOverlappedResult.argtypes = [FT_HANDLE, LPOVERLAPPED, LPDWORD, BOOL]
# FT_W32_GetOverlappedResult.__doc__ = """BOOL FT_W32_GetOverlappedResult(FT_HANDLE ftHandle, LPOVERLAPPED lpOverlapped, LPDWORD lpdwBytesTransferred, BOOL bWait)
# ftd2xx.h:674"""
# # ftd2xx.h 679
# FT_W32_CancelIo = LIB_FTD2XX.FT_W32_CancelIo
# FT_W32_CancelIo.restype = BOOL
# # FT_W32_CancelIo(ftHandle)
# FT_W32_CancelIo.argtypes = [FT_HANDLE]
# FT_W32_CancelIo.__doc__ = """BOOL FT_W32_CancelIo(FT_HANDLE ftHandle)
# ftd2xx.h:679"""
# # ftd2xx.h 685
#
#
# # ftd2xx.h 741
# FT_W32_ClearCommBreak = LIB_FTD2XX.FT_W32_ClearCommBreak
# FT_W32_ClearCommBreak.restype = BOOL
# # FT_W32_ClearCommBreak(ftHandle)
# FT_W32_ClearCommBreak.argtypes = [FT_HANDLE]
# FT_W32_ClearCommBreak.__doc__ = """BOOL FT_W32_ClearCommBreak(FT_HANDLE ftHandle)
# ftd2xx.h:741"""
# # ftd2xx.h 748
# FT_W32_ClearCommError = LIB_FTD2XX.FT_W32_ClearCommError
# FT_W32_ClearCommError.restype = BOOL
# # FT_W32_ClearCommError(ftHandle, lpdwErrors, lpftComstat)
# FT_W32_ClearCommError.argtypes = [FT_HANDLE, LPDWORD, LPFTCOMSTAT]
# FT_W32_ClearCommError.__doc__ = """BOOL FT_W32_ClearCommError(FT_HANDLE ftHandle, LPDWORD lpdwErrors, LPFTCOMSTAT lpftComstat)
# ftd2xx.h:748"""
# # ftd2xx.h 754
# FT_W32_EscapeCommFunction = LIB_FTD2XX.FT_W32_EscapeCommFunction
# FT_W32_EscapeCommFunction.restype = BOOL
# # FT_W32_EscapeCommFunction(ftHandle, dwFunc)
# FT_W32_EscapeCommFunction.argtypes = [FT_HANDLE, DWORD]
# FT_W32_EscapeCommFunction.__doc__ = """BOOL FT_W32_EscapeCommFunction(FT_HANDLE ftHandle, DWORD dwFunc)
# ftd2xx.h:754"""
# # ftd2xx.h 760
# FT_W32_GetCommModemStatus = LIB_FTD2XX.FT_W32_GetCommModemStatus
# FT_W32_GetCommModemStatus.restype = BOOL
# # FT_W32_GetCommModemStatus(ftHandle, lpdwModemStatus)
# FT_W32_GetCommModemStatus.argtypes = [FT_HANDLE, LPDWORD]
# FT_W32_GetCommModemStatus.__doc__ = """BOOL FT_W32_GetCommModemStatus(FT_HANDLE ftHandle, LPDWORD lpdwModemStatus)
# ftd2xx.h:760"""
# # ftd2xx.h 766
# FT_W32_GetCommState = LIB_FTD2XX.FT_W32_GetCommState
# FT_W32_GetCommState.restype = BOOL
# # FT_W32_GetCommState(ftHandle, lpftDcb)
# FT_W32_GetCommState.argtypes = [FT_HANDLE, LPFTDCB]
# FT_W32_GetCommState.__doc__ = """BOOL FT_W32_GetCommState(FT_HANDLE ftHandle, LPFTDCB lpftDcb)
# ftd2xx.h:766"""
# # ftd2xx.h 772
# FT_W32_GetCommTimeouts = LIB_FTD2XX.FT_W32_GetCommTimeouts
# FT_W32_GetCommTimeouts.restype = BOOL
# # FT_W32_GetCommTimeouts(ftHandle, pTimeouts)
# FT_W32_GetCommTimeouts.argtypes = [FT_HANDLE, POINTER(FTTIMEOUTS)]
# FT_W32_GetCommTimeouts.__doc__ = """BOOL FT_W32_GetCommTimeouts(FT_HANDLE ftHandle, FTTIMEOUTS * pTimeouts)
# ftd2xx.h:772"""
# # ftd2xx.h 778
# FT_W32_PurgeComm = LIB_FTD2XX.FT_W32_PurgeComm
# FT_W32_PurgeComm.restype = BOOL
# # FT_W32_PurgeComm(ftHandle, dwMask)
# FT_W32_PurgeComm.argtypes = [FT_HANDLE, DWORD]
# FT_W32_PurgeComm.__doc__ = """BOOL FT_W32_PurgeComm(FT_HANDLE ftHandle, DWORD dwMask)
# ftd2xx.h:778"""
# # ftd2xx.h 783
# FT_W32_SetCommBreak = LIB_FTD2XX.FT_W32_SetCommBreak
# FT_W32_SetCommBreak.restype = BOOL
# # FT_W32_SetCommBreak(ftHandle)
# FT_W32_SetCommBreak.argtypes = [FT_HANDLE]
# FT_W32_SetCommBreak.__doc__ = """BOOL FT_W32_SetCommBreak(FT_HANDLE ftHandle)
# ftd2xx.h:783"""
# # ftd2xx.h 789
# FT_W32_SetCommMask = LIB_FTD2XX.FT_W32_SetCommMask
# FT_W32_SetCommMask.restype = BOOL
# # FT_W32_SetCommMask(ftHandle, ulEventMask)
# FT_W32_SetCommMask.argtypes = [FT_HANDLE, ULONG]
# FT_W32_SetCommMask.__doc__ = """BOOL FT_W32_SetCommMask(FT_HANDLE ftHandle, ULONG ulEventMask)
# ftd2xx.h:789"""
# # ftd2xx.h 795
# FT_W32_SetCommState = LIB_FTD2XX.FT_W32_SetCommState
# FT_W32_SetCommState.restype = BOOL
# # FT_W32_SetCommState(ftHandle, lpftDcb)
# FT_W32_SetCommState.argtypes = [FT_HANDLE, LPFTDCB]
# FT_W32_SetCommState.__doc__ = """BOOL FT_W32_SetCommState(FT_HANDLE ftHandle, LPFTDCB lpftDcb)
# ftd2xx.h:795"""
# # ftd2xx.h 801
# FT_W32_SetCommTimeouts = LIB_FTD2XX.FT_W32_SetCommTimeouts
# FT_W32_SetCommTimeouts.restype = BOOL
# # FT_W32_SetCommTimeouts(ftHandle, pTimeouts)
# FT_W32_SetCommTimeouts.argtypes = [FT_HANDLE, POINTER(FTTIMEOUTS)]
# FT_W32_SetCommTimeouts.__doc__ = """BOOL FT_W32_SetCommTimeouts(FT_HANDLE ftHandle, FTTIMEOUTS * pTimeouts)
# ftd2xx.h:801"""
# # ftd2xx.h 808
# FT_W32_SetupComm = LIB_FTD2XX.FT_W32_SetupComm
# FT_W32_SetupComm.restype = BOOL
# # FT_W32_SetupComm(ftHandle, dwReadBufferSize, dwWriteBufferSize)
# FT_W32_SetupComm.argtypes = [FT_HANDLE, DWORD, DWORD]
# FT_W32_SetupComm.__doc__ = """BOOL FT_W32_SetupComm(FT_HANDLE ftHandle, DWORD dwReadBufferSize, DWORD dwWriteBufferSize)
# ftd2xx.h:808"""
# # ftd2xx.h 815
# FT_W32_WaitCommEvent = LIB_FTD2XX.FT_W32_WaitCommEvent
# FT_W32_WaitCommEvent.restype = BOOL
# # FT_W32_WaitCommEvent(ftHandle, pulEvent, lpOverlapped)
# FT_W32_WaitCommEvent.argtypes = [FT_HANDLE, PULONG, LPOVERLAPPED]
# FT_W32_WaitCommEvent.__doc__ = """BOOL FT_W32_WaitCommEvent(FT_HANDLE ftHandle, PULONG pulEvent, LPOVERLAPPED lpOverlapped)
# ftd2xx.h:815"""
# # ftd2xx.h 822


__all__ = [
    "FT_W32_CreateFile",
    # "FT_W32_CloseHandle",
    # "FT_W32_ReadFile",
    # "FT_W32_WriteFile",
    # "FT_W32_GetOverlappedResult",
    # "FT_W32_EscapeCommFunction",
    # "FT_W32_GetCommModemStatus",
    # "FT_W32_SetupComm",
    # "FT_W32_SetCommState",
    # "FT_W32_GetCommState",
    # "FT_W32_SetCommTimeouts",
    # "FT_W32_GetCommTimeouts",
    # "FT_W32_SetCommBreak",
    # "FT_W32_ClearCommBreak",
    # "FT_W32_SetCommMask",
    # "FT_W32_GetCommMask",
    # "FT_W32_WaitCommEvent",
    # "FT_W32_PurgeComm",
    # "FT_W32_GetLastError",
    # "FT_W32_ClearCommError",
    # "FT_W32_CancelIo",
]
