"""D2XX Classic Functions"""
from ctypes import POINTER
from .typedefs import (
    FT_HANDLE,
    FT_STATUS,
    FT_DEVICE,
    LPOVERLAPPED,
    FT_DEVICE_LIST_INFO_NODE,
    UCHAR,
    USHORT,
    WORD,
    DWORD,
    INT,
    ULONG,
    PVOID,
    PCHAR,
    PULONG,
    LPVOID,
    LPDWORD,
    LPLONG,
)

# pylint: disable=C0103
# pylint: disable=unused-argument
# pylint: disable=too-many-arguments


def FT_SetVIDPID(dwVID: DWORD, dwPID: DWORD) -> FT_STATUS:
    """A command to include a custom VID and PID combination within the internal device list table.

    Args:
        dwVID (DWORD): Device Vendor ID (VID).
        dwPID (DWORD): Device Product ID (PID).

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_GetVIDPID(pdwVID: POINTER(DWORD), pdwPID: POINTER(DWORD)) -> FT_STATUS:
    """A command to retrieve the current VID and PID combination from within the internal device
    list table.

    Args:
        pdwVID (POINTER(DWORD)): Pointer to DWORD that will contain the internal VID.
        pdwPID (POINTER(DWORD)): Pointer to DWORD that will contain the internal PID.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_CreateDeviceInfoList(lpdwNumDevs: LPDWORD) -> FT_STATUS:
    """This function builds a device information list and returns the number of D2XX devices
    connected to the system. The list contains information about both unopen and open devices.

    Args:
        lpdwNumDev (LPDWORD): Pointer to unsigned long to store the number of devices connected.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_GetDeviceInfoList(
    pDest: POINTER(FT_DEVICE_LIST_INFO_NODE), lpdwNumDevs: LPDWORD
) -> FT_STATUS:
    """This function returns a device information list and the number of D2XX devices in the list.

    Args:
        pDest (POINTER(FT_DEVICE_LIST_INFO_NODE)): Pointer to an array of FT_DEVICE_LIST_INFO_NODE
            structures.
        lpdwNumDevs (LPDWORD): Pointer to the number of elements in the array.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_GetDeviceInfoDetail(
    dwIndex: DWORD,
    lpdwFlags: LPDWORD,
    lpdwType: LPDWORD,
    lpdwID: LPDWORD,
    lpdwLocId: LPDWORD,
    lpSerialNumber: LPVOID,
    lpDescription: LPVOID,
    pftHandle: POINTER(FT_HANDLE),
) -> FT_STATUS:
    """This function returns an entry from the device information list.

    Args:
        dwIndex (DWORD): Index of the entry in the device info list.
        lpdwFlags (LPDWORD): Pointer to unsigned long to store the flag value.
        lpdwType (LPDWORD): Pointer to unsigned long to store device type.
        lpdwID (LPDWORD): Pointer to unsigned long to store device ID.
        lpdwLocId (LPDWORD): Pointer to unsigned long to store the device location ID.
        lpSerialNumber (LPVOID): Pointer to buffer to store device serial number as a
            nullterminated string.
        lpDescription (LPVOID): Pointer to buffer to store device description as a null-terminated
            string.
        pftHandle (POINTER(FT_HANDLE)): Pointer to a variable of type FT_HANDLE where the handle
            will be stored. This handle must be used to access the device.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_ListDevices(pvArg1: PVOID, pvArg2: PVOID, dwFlags: DWORD) -> FT_STATUS:
    """Gets information concerning the devices currently connected. This function can return
    information such as the number of devices connected, the device serial number and device
    description strings, and the location IDs of connected devices.

    Args:
        pvArg1 (PVOID): Meaning depends on dwFlags.
        pvArg2 (PVOID): Meaning depends on dwFlags.
        dwFlags (DWORD): Determines the format of returned information.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_Open(iDevice: INT, ftHandle: POINTER(FT_HANDLE)) -> FT_STATUS:
    """Open the device and return a handle which will be used for subsequent accesses.

    Args:
        deviceNumber (INT): Index of the device to open. Indices are 0 based.
        ftHandle (POINTER(FT_HANDLE)): Pointer to a variable of type FT_HANDLE where the handle
            will be stored. This handle must be used to access the device.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_OpenEx(pvArg1: PVOID, dwFlags: DWORD, ftHandle: POINTER(FT_HANDLE)) -> FT_STATUS:
    """Open the specified device and return a handle that will be used for subsequent accesses. The
    device can be specified by its serial number, device description or location.

    This function can also be used to open multiple devices simultaneously. Multiple devices can be
    specified by serial number, device description or location ID (location information derived
    from the physical location of a device on USB). Location IDs for specific USB ports can be
    obtained using the utility USBView and are given in hexadecimal format. Location IDs for
    devices connected to a system can be obtained by calling FT_GetDeviceInfoList or FT_ListDevices
    with the appropriate flags.

    Args:
        pvArg1 (PVOID): Pointer to an argument whose type depends on the value of dwFlags. It is
            normally be interpreted as a pointer to a null terminated string.
        dwFlags (DWORD): FT_OPEN_BY_SERIAL_NUMBER, FT_OPEN_BY_DESCRIPTION or FT_OPEN_BY_LOCATION.
        ftHandle (POINTER(FT_HANDLE)): Pointer to a variable of type FT_HANDLE where the handle
        will be stored. This handle must be used to access the device.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_Close(ftHandle: FT_HANDLE) -> FT_STATUS:
    """Close an open device.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_Read(
    ftHandle: FT_HANDLE,
    lpBuffer: LPVOID,
    dwBytesToRead: DWORD,
    lpdwBytesReturned: LPDWORD,
) -> FT_STATUS:
    """Read data from the device.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        lpBuffer (LPVOID): Pointer to the buffer that receives the data from the device.
        dwBytesToRead (DWORD): Number of bytes to be read from the device.
        lpdwBytesReturned (LPDWORD): Pointer to a variable of type DWORD which receives the number
            of bytes read from the device.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_Write(
    ftHandle: FT_HANDLE,
    lpBuffer: LPVOID,
    dwBytesToWrite: DWORD,
    lpdwBytesWritten,
) -> FT_STATUS:
    """Write data to the device.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        lpBuffer (LPVOID): Pointer to the buffer that contains the data to be written to the
            device.
        dwBytesToWrite (DWORD): Number of bytes to write to the device.
        lpdwBytesWritten (LPDWORD): Pointer to a variable of type DWORD which receives the number
            of bytes written to the device.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_SetBaudRate(ftHandle: FT_HANDLE, dwBaudRate: ULONG) -> FT_STATUS:
    """This function sets the baud rate for the device.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        dwBaudRate (DWORD): Baud rate.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_SetDivisor(ftHandle: FT_HANDLE, usDivisor: USHORT) -> FT_STATUS:
    """This function sets the baud rate for the device. It is used to set non-standard baud rates.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        usDivisor (USHORT): Divisor.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_SetDataCharacteristics(
    ftHandle: FT_HANDLE,
    uWordLength: UCHAR,
    uStopBits: UCHAR,
    uParity: UCHAR,
) -> FT_STATUS:
    """This function sets the data characteristics for the device.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        uWordLength (UCHAR): Number of bits per word - must be FT_BITS_8 or FT_BITS_7.
        uStopBits (UCHAR): Number of stop bits - must be FT_STOP_BITS_1 or FT_STOP_BITS_2.
        uParity (UCHAR): Parity - must be FT_PARITY_NONE, FT_PARITY_ODD, FT_PARITY_EVEN,
            FT_PARITY_MARK or FT_PARITY SPACE.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_SetTimeouts(
    ftHandle: FT_HANDLE, dwReadTimeout: ULONG, dwWriteTimeout: ULONG
) -> FT_STATUS:
    """This function sets the read and write timeouts for the device.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        dwReadTimeout (ULONG): Read timeout in milliseconds.
        dwWriteTimeout (ULONG): Write timeout in milliseconds.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_SetFlowControl(
    ftHandle: FT_HANDLE,
    usFlowControl: USHORT,
    uXonChar: UCHAR,
    uXoffChar: UCHAR,
) -> FT_STATUS:
    """This function sets the flow control for the device.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        usFlowControl (USHORT): Must be one of FT_FLOW_NONE, FT_FLOW_RTS_CTS, FT_FLOW_DTR_DSR or
            FT_FLOW_XON_XOFF.
        uXonChar (UCHAR): Character used to signal Xon. Only used if flow control is
            FT_FLOW_XON_XOFF.
        uXoffChar (UCHAR): Character used to signal Xoff. Only used if flow control is
            FT_FLOW_XON_XOFF.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_SetDtr(ftHandle: FT_HANDLE) -> FT_STATUS:
    """This function sets the Data Terminal Ready (DTR) control signal.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_ClrDtr(ftHandle: FT_HANDLE) -> FT_STATUS:
    """This function clears the Data Terminal Ready (DTR) control signal.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_SetRts(ftHandle: FT_HANDLE) -> FT_STATUS:
    """This function sets the Request To Send (RTS) control signal.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_ClrRts(ftHandle: FT_HANDLE) -> FT_STATUS:
    """This function clears the Request To Send (RTS) control signal.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_GetModemStatus(ftHandle: FT_HANDLE, lpdwModemStatus: PULONG) -> FT_STATUS:
    """Gets the modem status and line status from the device.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        lpdwModemStatus (PULONG): Pointer to a variable of type DWORD which receives the modem
            status and line status from the device.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_GetQueueStatus(
    ftHandle: FT_HANDLE, lpdwAmountInRxQueue: POINTER(DWORD)
) -> FT_STATUS:
    """Gets the number of bytes in the receive queue.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        lpdwAmountInRxQueue (POINTER(DWORD))): Pointer to a variable of type DWORD which receives
            the number of bytes in the receive queue.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_GetDeviceInfo(
    ftHandle: FT_HANDLE,
    lpftDevice: POINTER(FT_DEVICE),
    lpdwID: LPDWORD,
    SerialNumber: PCHAR,
    Description: PCHAR,
    Dummy: LPVOID,
) -> FT_STATUS:
    """Get device information for an open device.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        lpftDevice (POINTER(FT_DEVICE)): Pointer to unsigned long to store device type.
        lpdwID (LPDWORD): Pointer to unsigned long to store device ID.
        pcSerialNumber (PCHAR): Pointer to buffer to store device serial number as a
            null-terminated string.
        pcDescription (PCHAR): Pointer to buffer to store device description as a null-terminated
            string.
        pvDummy (LPVOID): Reserved for future use - should be set to NULL.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_GetDriverVersion(ftHandle: FT_HANDLE, lpdwVersion: LPDWORD) -> FT_STATUS:
    """This function returns the D2XX driver version number.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        lpdwDriverVersion (LPDWORD): Pointer to the driver version number.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_GetLibraryVersion(lpdwVersion: LPDWORD) -> FT_STATUS:
    """This function returns D2XX DLL or library version number.

    Args:
        lpdwDLLVersion (LPDWORD): Pointer to the DLL or library version number.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_GetComPortNumber(ftHandle: FT_HANDLE, lpdwComPortNumber: LPLONG) -> FT_STATUS:
    """Retrieves the COM port associated with a device.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        lplComPortNumber (LPLONG): Pointer to a variable of type LONG which receives the COM port
            number associated with the device.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_GetStatus(
    ftHandle: FT_HANDLE,
    lpdwAmountInRxQueue: POINTER(DWORD),
    lpdwAmountInTxQueue: POINTER(DWORD),
    lpdwEventStatus: POINTER(DWORD),
) -> FT_STATUS:
    """Gets the device status including number of characters in the receive queue, number of
    characters in the transmit queue, and the current event status.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        lpdwAmountInRxQueue (POINTER(DWORD)): Pointer to a variable of type DWORD which receives
            the number of characters in the receive queue.
        lpdwAmountInTxQueue (POINTER(DWORD)): Pointer to a variable of type DWORD which receives
            the number of characters in the transmit queue.
        lpdwEventStatus (POINTER(DWORD)): Pointer to a variable of type DWORD which receives the
            current state of the event status.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_SetEventNotification(
    ftHandle: FT_HANDLE, dwEventMask: DWORD, pvArg: PVOID
) -> FT_STATUS:
    """Sets conditions for event notification.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        dwEventMask (DWORD): Conditions that cause the event to be set.
        pvArg (PVOID): Interpreted as the handle of an event.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_SetChars(
    ftHandle: FT_HANDLE,
    uEventChar: UCHAR,
    uEventCharEnabled: UCHAR,
    uErrorChar: UCHAR,
    uErrorCharEnabled: UCHAR,
) -> FT_STATUS:
    """This function sets the special characters for the device.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        uEventChar (UCHAR): Event character.
        uEventCharEnabled (UCHAR): 0 if event character disabled, non-zero otherwise.
        uErrorChar (UCHAR): Error character.
        uErrorCharEnabled (UCHAR): 0 if error character disabled, non-zero otherwise.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_SetBreakOn(ftHandle: FT_HANDLE) -> FT_STATUS:
    """Sets the BREAK condition for the device.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_SetBreakOff(ftHandle: FT_HANDLE) -> FT_STATUS:
    """Resets the BREAK condition for the device.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_Purge(ftHandle: FT_HANDLE, ulMask: ULONG) -> FT_STATUS:
    """This function purges receive and transmit buffers in the device.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        ulMask (ULONG): Combination of FT_PURGE_RX and FT_PURGE_TX.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_ResetDevice(ftHandle: FT_HANDLE) -> FT_STATUS:
    """This function sends a reset command to the device.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_ResetPort(ftHandle: FT_HANDLE) -> FT_STATUS:
    """Send a reset command to the port.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_CyclePort(ftHandle: FT_HANDLE) -> FT_STATUS:
    """Send a cycle command to the USB port.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_Rescan() -> FT_STATUS:
    """This function can be of use when trying to recover devices programatically.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_Reload(wVID: WORD, wPID: WORD) -> FT_STATUS:
    """This function forces a reload of the driver for devices with a specific VID and PID
    combination.

    Args:
        wVID (WORD): Vendor ID of the devices to reload the driver for.
        wPID (WORD): Product ID of the devices to reload the driver for.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_SetResetPipeRetryCount(ftHandle: FT_HANDLE, dwCount: DWORD) -> FT_STATUS:
    """Set the ResetPipeRetryCount value.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        dwCount (DWORD): Unsigned long containing required ResetPipeRetryCount.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_StopInTask(ftHandle: FT_HANDLE) -> FT_STATUS:
    """Stops the driver's IN task.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_RestartInTask(ftHandle: FT_HANDLE) -> FT_STATUS:
    """Restart the driver's IN task.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_SetDeadmanTimeout(ftHandle: FT_HANDLE, ulDeadmanTimeout: ULONG) -> FT_STATUS:
    """This function allows the maximum time in milliseconds that a USB request can remain
    outstanding to be set.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        ulDeadmanTimeout (ULONG): Deadman timeout value in milliseconds. Default value is 5000.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_IoCtl(
    ftHandle: FT_HANDLE,
    dwIoControlCode: DWORD,
    lpInBuf: LPVOID,
    nInBufSize: DWORD,
    lpOutBuf: LPVOID,
    nOutBufSize: DWORD,
    lpBytesReturned: LPDWORD,
    lpOverlapped: LPOVERLAPPED,
) -> FT_STATUS:
    """Undocumented function."""


def FT_SetWaitMask(ftHandle: FT_HANDLE, Mask: DWORD) -> FT_STATUS:
    """Undocumented function."""


def FT_WaitOnMask(ftHandle: FT_HANDLE, Mask: POINTER(DWORD)) -> FT_STATUS:
    """Undocumented function."""


def FT_GetEventStatus(ftHandle: FT_HANDLE, dwEventDWord: POINTER(DWORD)) -> FT_STATUS:
    """Undocumented function."""


__all__ = [
    "FT_SetVIDPID",  # Linux/Darwin only
    "FT_GetVIDPID",  # Linux/Darwin only
    "FT_CreateDeviceInfoList",
    "FT_GetDeviceInfoList",
    "FT_GetDeviceInfoDetail",
    "FT_ListDevices",
    "FT_Open",
    "FT_OpenEx",
    "FT_Close",
    "FT_Read",
    "FT_Write",
    "FT_SetBaudRate",
    "FT_SetDivisor",
    "FT_SetDataCharacteristics",
    "FT_SetTimeouts",
    "FT_SetFlowControl",
    "FT_SetDtr",
    "FT_ClrDtr",
    "FT_SetRts",
    "FT_ClrRts",
    "FT_GetModemStatus",
    "FT_GetQueueStatus",
    "FT_GetDeviceInfo",
    "FT_GetDriverVersion",  # Windows only
    "FT_GetLibraryVersion",  # Windows only
    "FT_GetComPortNumber",  # Windows only
    "FT_GetStatus",
    "FT_SetEventNotification",
    "FT_SetChars",
    "FT_SetBreakOn",
    "FT_SetBreakOff",
    "FT_Purge",
    "FT_ResetDevice",
    "FT_ResetPort",  # Windows only
    "FT_CyclePort",  # Windows only
    "FT_Rescan",  # Windows only
    "FT_Reload",  # Windows only
    "FT_SetResetPipeRetryCount",  # Windows only
    "FT_StopInTask",
    "FT_RestartInTask",
    "FT_SetDeadmanTimeout",
    "FT_IoCtl",  # Undocumented
    "FT_SetWaitMask",  # Undocumented
    "FT_WaitOnMask",  # Undocumented
    "FT_GetEventStatus",  # Undocumented
]
