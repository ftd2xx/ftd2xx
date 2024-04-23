"""
Module for accessing functions from FTD2XX in an easier to use
_pythonic_ way. For full documentation please refer to the FTDI
Programming Guide. This module is based on Pablo Bleyers d2xx module,
except this uses ctypes instead of an extension approach.
"""

from __future__ import annotations

import ctypes as c
import logging
import sys
from types import TracebackType
from typing import Any, Callable, ContextManager, TypedDict

from . import defines

if sys.platform == "win32":
    from . import _ftd2xx as _ft
elif sys.platform.startswith("linux"):
    from . import _ftd2xx_linux as _ft
elif sys.platform == "darwin":
    from . import _ftd2xx_darwin as _ft
else:
    raise Exception("Unknown platform")


ft_program_data = _ft.ft_program_data

LOGGER = logging.getLogger("ftd2xx")


class DeviceError(Exception):
    """Exception class for status messages"""

    def __init__(self, message: int | Any):
        super().__init__()
        if isinstance(message, int):
            self.message = defines.Status(message).name
        else:
            self.message = str(message)

    def __str__(self):
        return self.message

    def __reduce__(self):
        return type(self), (self.message,)


class DeviceInfoDetail(TypedDict):
    index: int
    flags: int
    type: int
    id: int
    location: int
    serial: bytes
    description: bytes
    handle: _ft.FT_HANDLE


class DeviceInfo(TypedDict):
    type: int
    id: int
    description: bytes
    serial: bytes


class ProgramData(TypedDict, total=False):
    Signature1: _ft.DWORD | int
    Signature2: _ft.DWORD | int
    Version: _ft.DWORD | int
    VendorId: _ft.WORD | int
    ProductId: _ft.WORD | int
    Manufacturer: _ft.STRING | int
    ManufacturerId: _ft.STRING | int
    Description: _ft.STRING | int
    SerialNumber: _ft.STRING | int
    MaxPower: _ft.WORD | int
    PnP: _ft.WORD | int
    SelfPowered: _ft.WORD | int
    RemoteWakeup: _ft.WORD | int
    Rev4: _ft.UCHAR | int
    IsoIn: _ft.UCHAR | int
    IsoOut: _ft.UCHAR | int
    PullDownEnable: _ft.UCHAR | int
    SerNumEnable: _ft.UCHAR | int
    USBVersionEnable: _ft.UCHAR | int
    USBVersion: _ft.WORD | int
    Rev5: _ft.UCHAR | int
    IsoInA: _ft.UCHAR | int
    IsoInB: _ft.UCHAR | int
    IsoOutA: _ft.UCHAR | int
    IsoOutB: _ft.UCHAR | int
    PullDownEnable5: _ft.UCHAR | int
    SerNumEnable5: _ft.UCHAR | int
    USBVersionEnable5: _ft.UCHAR | int
    USBVersion5: _ft.WORD | int
    AIsHighCurrent: _ft.UCHAR | int
    BIsHighCurrent: _ft.UCHAR | int
    IFAIsFifo: _ft.UCHAR | int
    IFAIsFifoTar: _ft.UCHAR | int
    IFAIsFastSer: _ft.UCHAR | int
    AIsVCP: _ft.UCHAR | int
    IFBIsFifo: _ft.UCHAR | int
    IFBIsFifoTar: _ft.UCHAR | int
    IFBIsFastSer: _ft.UCHAR | int
    BIsVCP: _ft.UCHAR | int
    UseExtOsc: _ft.UCHAR | int
    HighDriveIOs: _ft.UCHAR | int
    EndpointSize: _ft.UCHAR | int
    PullDownEnableR: _ft.UCHAR | int
    SerNumEnableR: _ft.UCHAR | int
    InvertTXD: _ft.UCHAR | int
    InvertRXD: _ft.UCHAR | int
    InvertRTS: _ft.UCHAR | int
    InvertCTS: _ft.UCHAR | int
    InvertDTR: _ft.UCHAR | int
    InvertDSR: _ft.UCHAR | int
    InvertDCD: _ft.UCHAR | int
    InvertRI: _ft.UCHAR | int
    Cbus0: _ft.UCHAR | int
    Cbus1: _ft.UCHAR | int
    Cbus2: _ft.UCHAR | int
    Cbus3: _ft.UCHAR | int
    Cbus4: _ft.UCHAR | int
    RIsVCP: _ft.UCHAR | int
    PullDownEnable7: _ft.UCHAR | int
    SerNumEnable7: _ft.UCHAR | int
    ALSlowSlew: _ft.UCHAR | int
    ALSchmittInput: _ft.UCHAR | int
    ALDriveCurrent: _ft.UCHAR | int
    AHSlowSlew: _ft.UCHAR | int
    AHSchmittInput: _ft.UCHAR | int
    AHDriveCurrent: _ft.UCHAR | int
    BLSlowSlew: _ft.UCHAR | int
    BLSchmittInput: _ft.UCHAR | int
    BLDriveCurrent: _ft.UCHAR | int
    BHSlowSlew: _ft.UCHAR | int
    BHSchmittInput: _ft.UCHAR | int
    BHDriveCurrent: _ft.UCHAR | int
    IFAIsFifo7: _ft.UCHAR | int
    IFAIsFifoTar7: _ft.UCHAR | int
    IFAIsFastSer7: _ft.UCHAR | int
    AIsVCP7: _ft.UCHAR | int
    IFBIsFifo7: _ft.UCHAR | int
    IFBIsFifoTar7: _ft.UCHAR | int
    IFBIsFastSer7: _ft.UCHAR | int
    BIsVCP7: _ft.UCHAR | int
    PowerSaveEnable: _ft.UCHAR | int
    PullDownEnable8: _ft.UCHAR | int
    SerNumEnable8: _ft.UCHAR | int
    ASlowSlew: _ft.UCHAR | int
    ASchmittInput: _ft.UCHAR | int
    ADriveCurrent: _ft.UCHAR | int
    BSlowSlew: _ft.UCHAR | int
    BSchmittInput: _ft.UCHAR | int
    BDriveCurrent: _ft.UCHAR | int
    CSlowSlew: _ft.UCHAR | int
    CSchmittInput: _ft.UCHAR | int
    CDriveCurrent: _ft.UCHAR | int
    DSlowSlew: _ft.UCHAR | int
    DSchmittInput: _ft.UCHAR | int
    DDriveCurrent: _ft.UCHAR | int
    ARIIsTXDEN: _ft.UCHAR | int
    BRIIsTXDEN: _ft.UCHAR | int
    CRIIsTXDEN: _ft.UCHAR | int
    DRIIsTXDEN: _ft.UCHAR | int
    AIsVCP8: _ft.UCHAR | int
    BIsVCP8: _ft.UCHAR | int
    CIsVCP8: _ft.UCHAR | int
    DIsVCP8: _ft.UCHAR | int


def call_ft(function: Callable, *args):
    """Call an FTDI function and check the status. Raise exception on error"""
    status = function(*args)
    if status != defines.Status.OK:
        raise DeviceError(status)


def listDevices(flags: int = 0) -> list[bytes] | None:
    """Return a list of serial numbers(default), descriptions or
    locations (Windows only) of the connected FTDI devices depending on value
    of flags"""
    n = _ft.DWORD()
    call_ft(_ft.FT_ListDevices, c.byref(n), None, _ft.DWORD(defines.LIST_NUMBER_ONLY))
    devcount = n.value
    LOGGER.debug("Found %i devices", devcount)
    if devcount:
        # since ctypes has no pointer arithmetic.
        bd = [
            c.create_string_buffer(defines.MAX_DESCRIPTION_SIZE)
            for i in range(devcount)
        ]

        # array of pointers to those strings, initially all NULL
        ba = (c.c_char_p * (devcount + 1))(*[c.addressof(x) for x in bd], None)
        # for i in range(devcount):
        #     ba[i] = c.c_char_p(bd[i])
        call_ft(_ft.FT_ListDevices, ba, c.byref(n), _ft.DWORD(defines.LIST_ALL | flags))
        return [res for res in ba[:devcount]]

    return None


def getLibraryVersion() -> int:
    """Return a long representing library version"""
    m = _ft.DWORD()
    call_ft(_ft.FT_GetLibraryVersion, c.byref(m))
    return m.value


def createDeviceInfoList() -> int:
    """Create the internal device info list and return number of entries"""
    m = _ft.DWORD()
    call_ft(_ft.FT_CreateDeviceInfoList, c.byref(m))
    return m.value


def getDeviceInfoDetail(devnum: int = 0, update: bool = True) -> DeviceInfoDetail:
    """Get an entry from the internal device info list. Set update to
    False to avoid a slow call to createDeviceInfoList."""
    flags = _ft.DWORD()
    typ = _ft.DWORD()
    dev_id = _ft.DWORD()
    location = _ft.DWORD()
    handle = _ft.FT_HANDLE()
    name = c.create_string_buffer(defines.MAX_DESCRIPTION_SIZE)
    description = c.create_string_buffer(defines.MAX_DESCRIPTION_SIZE)
    # createDeviceInfoList is slow, only run if update is True
    if update:
        createDeviceInfoList()
    call_ft(
        _ft.FT_GetDeviceInfoDetail,
        _ft.DWORD(devnum),
        c.byref(flags),
        c.byref(typ),
        c.byref(dev_id),
        c.byref(location),
        name,
        description,
        c.byref(handle),
    )
    return {
        "index": devnum,
        "flags": flags.value,
        "type": typ.value,
        "id": dev_id.value,
        "location": location.value,
        "serial": name.value,
        "description": description.value,
        "handle": handle,
    }


def open(dev: int = 0, update: bool = True) -> FTD2XX:
    """Open a handle to a usb device by index and return an FTD2XX instance for
    it. Set update to False to avoid a slow call to createDeviceInfoList.

    Args:
        dev (int): The device number to open.
        update (bool): Set to False to disable automatic call to createDeviceInfoList.

    Raises:
        DeviceError: If the device cannot be opened.

    Returns:
        An instance of the FTD2XX class if successful. Use it as a context manager.

    Example:
        with open(0, False) as dev:
            dev.write(b"Hello World")
    """
    h = _ft.FT_HANDLE()
    call_ft(_ft.FT_Open, dev, c.byref(h))
    return FTD2XX(h, update=update)


def openEx(
    id_str: bytes, flags: int = defines.OPEN_BY_SERIAL_NUMBER, update: bool = True
) -> FTD2XX:
    """Open a handle to a usb device by serial number(default), description or
    location(Windows only) depending on value of flags and return an FTD2XX
    instance for it. Set update to False to avoid a slow call to createDeviceInfoList.

    Args:
        id_str (bytes): The ID string from listDevices.
        flags (int): Flag (consult D2XX Guide). Defaults to OPEN_BY_SERIAL_NUMBER.
        update (bool): Set to False to disable automatic call to createDeviceInfoList.

    Raises:
        DeviceError: If the device cannot be opened.

    Returns:
        An instance of the FTD2XX class if successful. Use it as a context manager.

    Example:
        with openEx(b"MyDevice", update=False) as dev:
            dev.write(b"Hello World")

    """
    h = _ft.FT_HANDLE()
    call_ft(_ft.FT_OpenEx, id_str, _ft.DWORD(flags), c.byref(h))
    return FTD2XX(h, update=update)


if sys.platform == "win32":
    from win32con import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING

    def w32CreateFile(
        name: bytes,
        access: int = GENERIC_READ | GENERIC_WRITE,
        flags: int = defines.OPEN_BY_SERIAL_NUMBER,
    ):
        return FTD2XX(
            _ft.FT_W32_CreateFile(
                _ft.STRING(name),
                _ft.DWORD(access),
                _ft.DWORD(0),
                None,
                _ft.DWORD(OPEN_EXISTING),
                _ft.DWORD(flags),
                _ft.HANDLE(0),
            )
        )

else:

    def getVIDPID() -> tuple[int, int]:
        """Linux only. Get the VID and PID of the device"""
        vid = _ft.DWORD()
        pid = _ft.DWORD()
        call_ft(_ft.FT_GetVIDPID, c.byref(vid), c.byref(pid))
        return (vid.value, pid.value)

    def setVIDPID(vid, pid):
        """Linux only. Set the VID and PID of the device"""
        call_ft(_ft.FT_SetVIDPID, _ft.DWORD(vid), _ft.DWORD(pid))
        return None


class FTD2XX(ContextManager["FTD2XX"]):
    """Class for communicating with an FTDI device

    Use :any:`open` or :any:`openEx` to create an instance of this class.
    """

    handle: _ft.FT_HANDLE
    status: int

    def __init__(self, handle: _ft.FT_HANDLE, update: bool = True):
        """Create an instance of the FTD2XX class with the given device handle
        and populate the device info in the instance dictionary.

        Args:
            update (bool): Set False to disable automatic (slow) call to
                            createDeviceInfoList

        """
        self.handle = handle
        self.status = 1
        # createDeviceInfoList is slow, only run if update is True
        if update:
            createDeviceInfoList()
        self.__dict__.update(self.getDeviceInfo())

    def close(self) -> None:
        """Close the device handle"""
        call_ft(_ft.FT_Close, self.handle)
        self.status = 0

    def read(self, nchars: int, raw: bool = True) -> bytes:
        """Read up to nchars bytes of data from the device. Can return fewer if
        timedout. Use getQueueStatus to find how many bytes are available"""
        b_read = _ft.DWORD()
        b = c.create_string_buffer(nchars)
        call_ft(_ft.FT_Read, self.handle, b, nchars, c.byref(b_read))
        return b.raw[: b_read.value] if raw else b.value[: b_read.value]

    def write(self, data: bytes):
        """Send the data to the device. Data must be a string representing the
        bytes to be sent"""
        w = _ft.DWORD()
        call_ft(_ft.FT_Write, self.handle, data, len(data), c.byref(w))
        return w.value

    def ioctl(self):
        """Not implemented"""
        raise NotImplementedError

    def setBaudRate(self, baud: int) -> None:
        """Set the baud rate"""
        call_ft(_ft.FT_SetBaudRate, self.handle, _ft.DWORD(baud))

    def setDivisor(self, div: int):
        """Set the clock divider. The clock will be set to 6e6/(div + 1)."""
        call_ft(_ft.FT_SetDivisor, self.handle, _ft.USHORT(div))

    def setDataCharacteristics(self, wordlen: int, stopbits: int, parity: int):
        """Set the data characteristics for UART"""
        call_ft(
            _ft.FT_SetDataCharacteristics,
            self.handle,
            _ft.UCHAR(wordlen),
            _ft.UCHAR(stopbits),
            _ft.UCHAR(parity),
        )

    def setFlowControl(self, flowcontrol: int, xon: int = -1, xoff: int = -1):
        """Set the flow control for UART"""
        if flowcontrol == defines.FLOW_XON_XOFF and (xon == -1 or xoff == -1):
            raise ValueError
        call_ft(
            _ft.FT_SetFlowControl,
            self.handle,
            _ft.USHORT(flowcontrol),
            _ft.UCHAR(xon),
            _ft.UCHAR(xoff),
        )

    def resetDevice(self):
        """Reset the device"""
        call_ft(_ft.FT_ResetDevice, self.handle)

    def setDtr(self):
        """Set the DTR (Data Terminal Ready) signal of the FTDI device."""
        call_ft(_ft.FT_SetDtr, self.handle)

    def clrDtr(self):
        """Clear the DTR signal of the FTDI device."""
        call_ft(_ft.FT_ClrDtr, self.handle)

    def setRts(self):
        """Set the RTS (Request To Send) signal of the FTDI device."""
        call_ft(_ft.FT_SetRts, self.handle)

    def clrRts(self):
        """Clear the RTS signal of the FTDI device."""
        call_ft(_ft.FT_ClrRts, self.handle)

    def getModemStatus(self) -> defines.ModemStatus:
        """Get the modem status of the FTDI device."""
        m = _ft.DWORD()
        call_ft(_ft.FT_GetModemStatus, self.handle, c.byref(m))
        return defines.ModemStatus(m.value & 0xFFFF)

    def setChars(self, evch: int, evch_en: int, erch: int, erch_en: int):
        """Set the event and error characters for UART"""
        call_ft(
            _ft.FT_SetChars,
            self.handle,
            _ft.UCHAR(evch),
            _ft.UCHAR(evch_en),
            _ft.UCHAR(erch),
            _ft.UCHAR(erch_en),
        )

    def purge(self, mask: int = 0):
        """Purge the receive and/or transmit buffers"""
        if not mask:
            mask = defines.PURGE_RX | defines.PURGE_TX
        call_ft(_ft.FT_Purge, self.handle, _ft.DWORD(mask))

    def setTimeouts(self, read: int, write: int):
        """Set the read and write timeouts in milliseconds"""
        call_ft(_ft.FT_SetTimeouts, self.handle, _ft.DWORD(read), _ft.DWORD(write))

    def setDeadmanTimeout(self, timeout: int):
        """Set the deadman timeout in milliseconds"""
        call_ft(_ft.FT_SetDeadmanTimeout, self.handle, _ft.DWORD(timeout))

    def getQueueStatus(self) -> int:
        """Get number of bytes in receive queue."""
        rxQAmount = _ft.DWORD()
        call_ft(_ft.FT_GetQueueStatus, self.handle, c.byref(rxQAmount))
        return rxQAmount.value

    def setEventNotification(self, evtmask: int, evthandle):
        call_ft(
            _ft.FT_SetEventNotification,
            self.handle,
            _ft.DWORD(evtmask),
            _ft.HANDLE(evthandle),
        )

    def getStatus(self):
        """Return a 3-tuple of rx queue bytes, tx queue bytes and event
        status"""
        rxQAmount = _ft.DWORD()
        txQAmount = _ft.DWORD()
        evtStatus = _ft.DWORD()
        call_ft(
            _ft.FT_GetStatus,
            self.handle,
            c.byref(rxQAmount),
            c.byref(txQAmount),
            c.byref(evtStatus),
        )
        return (rxQAmount.value, txQAmount.value, evtStatus.value)

    def setBreakOn(self):
        call_ft(_ft.FT_SetBreakOn, self.handle)

    def setBreakOff(self):
        call_ft(_ft.FT_SetBreakOff, self.handle)

    def setWaitMask(self, mask: int):
        call_ft(_ft.FT_SetWaitMask, self.handle, _ft.DWORD(mask))

    def waitOnMask(self):
        mask = _ft.DWORD()
        call_ft(_ft.FT_WaitOnMask, self.handle, c.byref(mask))
        return mask.value

    def getEventStatus(self):
        evtStatus = _ft.DWORD()
        call_ft(_ft.FT_GetEventStatus, self.handle, c.byref(evtStatus))
        return evtStatus.value

    def setLatencyTimer(self, latency: int):
        call_ft(_ft.FT_SetLatencyTimer, self.handle, _ft.UCHAR(latency))

    def getLatencyTimer(self) -> int:
        latency = _ft.UCHAR()
        call_ft(_ft.FT_GetLatencyTimer, self.handle, c.byref(latency))
        return latency.value

    def setBitMode(self, mask: int, enable: int):
        call_ft(_ft.FT_SetBitMode, self.handle, _ft.UCHAR(mask), _ft.UCHAR(enable))

    def getBitMode(self) -> int:
        mask = _ft.UCHAR()
        call_ft(_ft.FT_GetBitMode, self.handle, c.byref(mask))
        return mask.value

    def setUSBParameters(self, in_tx_size: int, out_tx_size: int = 0):
        """Set the USB request transfer sizes"""
        call_ft(
            _ft.FT_SetUSBParameters,
            self.handle,
            _ft.ULONG(in_tx_size),
            _ft.ULONG(out_tx_size),
        )

    def getDeviceInfo(self) -> DeviceInfo:
        """Returns a dictionary describing the device."""
        deviceType = _ft.DWORD()
        deviceId = _ft.DWORD()
        desc = c.create_string_buffer(defines.MAX_DESCRIPTION_SIZE)
        serial = c.create_string_buffer(defines.MAX_DESCRIPTION_SIZE)

        call_ft(
            _ft.FT_GetDeviceInfo,
            self.handle,
            c.byref(deviceType),
            c.byref(deviceId),
            serial,
            desc,
            None,
        )
        return {
            "type": deviceType.value,
            "id": deviceId.value,
            "description": desc.value,
            "serial": serial.value,
        }

    def stopInTask(self):
        call_ft(_ft.FT_StopInTask, self.handle)

    def restartInTask(self):
        call_ft(_ft.FT_RestartInTask, self.handle)

    def setRestPipeRetryCount(self, count):
        call_ft(_ft.FT_SetResetPipeRetryCount, self.handle, _ft.DWORD(count))

    def resetPort(self):
        call_ft(_ft.FT_ResetPort, self.handle)

    def cyclePort(self):
        call_ft(_ft.FT_CyclePort, self.handle)

    def getDriverVersion(self) -> int:
        driver = _ft.DWORD()
        call_ft(_ft.FT_GetDriverVersion, self.handle, c.byref(driver))
        return driver.value

    def getComPortNumber(self) -> int:
        """Return a long representing the COM port number"""
        m = _ft.LONG()
        try:
            call_ft(_ft.FT_GetComPortNumber, self.handle, c.byref(m))
        except AttributeError as exc:
            raise Exception("FT_GetComPortNumber is only available on windows") from exc
        return m.value

    def eeProgram(self, progdata: _ft.ft_program_data | None = None, **kwds) -> None:
        """Program the EEPROM with custom data. If SerialNumber is null, a new
        serial number is generated from ManufacturerId"""
        if progdata is None:
            progdata = ft_program_data(**kwds)
        #        if self.devInfo['type'] == 4:
        #            version = 1
        #        elif self.devInfo['type'] == 5:
        #            version = 2
        #        else:
        #            version = 0
        progdata.Signature1 = _ft.DWORD(0)
        progdata.Signature2 = _ft.DWORD(0xFFFFFFFF)
        progdata.Version = _ft.DWORD(2)
        call_ft(_ft.FT_EE_Program, self.handle, progdata)

    def eeRead(self) -> _ft.ft_program_data:
        """Get the program information from the EEPROM"""
        #        if self.devInfo['type'] == 4:
        #            version = 1
        #        elif self.devInfo['type'] == 5:
        #            version = 2
        #        else:
        #            version = 0

        Manufacturer = c.create_string_buffer(defines.MAX_DESCRIPTION_SIZE)
        ManufacturerId = c.create_string_buffer(defines.MAX_DESCRIPTION_SIZE)
        Description = c.create_string_buffer(defines.MAX_DESCRIPTION_SIZE)
        SerialNumber = c.create_string_buffer(defines.MAX_DESCRIPTION_SIZE)
        progdata = ft_program_data(
            **ProgramData(
                Signature1=0,
                Signature2=0xFFFFFFFF,
                Version=4,
                Manufacturer=c.cast(Manufacturer, c.c_char_p),
                ManufacturerId=c.cast(ManufacturerId, c.c_char_p),
                Description=c.cast(Description, c.c_char_p),
                SerialNumber=c.cast(SerialNumber, c.c_char_p),
            )
        )

        call_ft(_ft.FT_EE_Read, self.handle, c.byref(progdata))
        return progdata

    def eeUASize(self) -> int:
        """Get the EEPROM user area size"""
        uasize = _ft.DWORD()
        call_ft(_ft.FT_EE_UASize, self.handle, c.byref(uasize))
        return uasize.value

    def eeUAWrite(self, data: bytes) -> None:
        """Write data to the EEPROM user area. data must be a bytes object with
        appropriate byte values"""
        buf = (c.c_ubyte * len(data)).from_buffer_copy(data)
        call_ft(_ft.FT_EE_UAWrite, self.handle, buf, len(data))

    def eeUARead(self, b_to_read: int) -> bytes:
        """Read b_to_read bytes from the EEPROM user area"""
        b_read = _ft.DWORD()
        # buf = c.create_string_buffer(b_to_read)
        buf = (c.c_ubyte * (b_to_read + 1))()
        call_ft(
            _ft.FT_EE_UARead,
            self.handle,
            buf,
            b_to_read,
            c.byref(b_read),
        )
        return bytes(buf[: b_read.value])

    def __exit__(
        self,
        __exc_type: type[BaseException] | None,
        __exc_value: BaseException | None,
        __traceback: TracebackType | None,
    ) -> bool | None:
        """Close the device when exiting the context manager"""
        self.close()
        return super().__exit__(__exc_type, __exc_value, __traceback)


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
    __all__ += ["w32CreateFile"]
else:
    __all__ += ["getVIDPID", "setVIDPID"]
