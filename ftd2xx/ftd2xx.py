"""
Module for accessing functions from FTD2XX in an easier to use
_pythonic_ way. For full documentation please refer to the FTDI
Programming Guide. This module is based on Pablo Bleyers d2xx module,
except this uses ctypes instead of an extension approach.
"""
import logging
import sys
from builtins import range
from contextlib import AbstractContextManager
from types import TracebackType
from typing import Any, Callable, List, Optional, Tuple, Type, Union
import ctypes as c
from . import defines
from . import typedefs as _t
from . import _ftd2xx as _ft


if sys.version_info >= (3, 8, 0):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ft_program_data = _t.ft_program_data

LOGGER = logging.getLogger("ftd2xx")


class DeviceError(Exception):
    """Exception class for status messages"""

    def __init__(self, message: Union[int, Any]):
        super().__init__()
        if isinstance(message, int):
            self.message = defines.Status(message).name
        else:
            self.message = str(message)

    def __str__(self):
        return self.message


class DeviceInfoDetail(TypedDict):
    index: int
    flags: int
    type: int
    id: int
    location: int
    serial: bytes
    description: bytes
    handle: _t.FT_HANDLE


class DeviceInfo(TypedDict):
    type: int
    id: int
    description: bytes
    serial: bytes


class ProgramData(TypedDict, total=False):
    Signature1: Union[_t.DWORD, int]
    Signature2: Union[_t.DWORD, int]
    Version: Union[_t.DWORD, int]
    VendorId: Union[_t.WORD, int]
    ProductId: Union[_t.WORD, int]
    Manufacturer: Union[_t.STRING, int]
    ManufacturerId: Union[_t.STRING, int]
    Description: Union[_t.STRING, int]
    SerialNumber: Union[_t.STRING, int]
    MaxPower: Union[_t.WORD, int]
    PnP: Union[_t.WORD, int]
    SelfPowered: Union[_t.WORD, int]
    RemoteWakeup: Union[_t.WORD, int]
    Rev4: Union[_t.UCHAR, int]
    IsoIn: Union[_t.UCHAR, int]
    IsoOut: Union[_t.UCHAR, int]
    PullDownEnable: Union[_t.UCHAR, int]
    SerNumEnable: Union[_t.UCHAR, int]
    USBVersionEnable: Union[_t.UCHAR, int]
    USBVersion: Union[_t.WORD, int]
    Rev5: Union[_t.UCHAR, int]
    IsoInA: Union[_t.UCHAR, int]
    IsoInB: Union[_t.UCHAR, int]
    IsoOutA: Union[_t.UCHAR, int]
    IsoOutB: Union[_t.UCHAR, int]
    PullDownEnable5: Union[_t.UCHAR, int]
    SerNumEnable5: Union[_t.UCHAR, int]
    USBVersionEnable5: Union[_t.UCHAR, int]
    USBVersion5: Union[_t.WORD, int]
    AIsHighCurrent: Union[_t.UCHAR, int]
    BIsHighCurrent: Union[_t.UCHAR, int]
    IFAIsFifo: Union[_t.UCHAR, int]
    IFAIsFifoTar: Union[_t.UCHAR, int]
    IFAIsFastSer: Union[_t.UCHAR, int]
    AIsVCP: Union[_t.UCHAR, int]
    IFBIsFifo: Union[_t.UCHAR, int]
    IFBIsFifoTar: Union[_t.UCHAR, int]
    IFBIsFastSer: Union[_t.UCHAR, int]
    BIsVCP: Union[_t.UCHAR, int]
    UseExtOsc: Union[_t.UCHAR, int]
    HighDriveIOs: Union[_t.UCHAR, int]
    EndpointSize: Union[_t.UCHAR, int]
    PullDownEnableR: Union[_t.UCHAR, int]
    SerNumEnableR: Union[_t.UCHAR, int]
    InvertTXD: Union[_t.UCHAR, int]
    InvertRXD: Union[_t.UCHAR, int]
    InvertRTS: Union[_t.UCHAR, int]
    InvertCTS: Union[_t.UCHAR, int]
    InvertDTR: Union[_t.UCHAR, int]
    InvertDSR: Union[_t.UCHAR, int]
    InvertDCD: Union[_t.UCHAR, int]
    InvertRI: Union[_t.UCHAR, int]
    Cbus0: Union[_t.UCHAR, int]
    Cbus1: Union[_t.UCHAR, int]
    Cbus2: Union[_t.UCHAR, int]
    Cbus3: Union[_t.UCHAR, int]
    Cbus4: Union[_t.UCHAR, int]
    RIsD2XX: Union[_t.UCHAR, int]

    @classmethod
    def from_struct(cls, data: c.Structure):
        inst = cls()
        for key in cls.__annotations__:
            inst[key] = getattr(data, key)
        return inst


class ProgramData_Common(TypedDict, total=False):
    deviceType: Union[_t.FT_DEVICE, defines.Device]
    VendorId: Union[_t.WORD, int]
    ProductId: Union[_t.WORD, int]
    SerNumEnable: Union[_t.UCHAR, int]
    MaxPower: Union[_t.WORD, int]
    SelfPowered: Union[_t.UCHAR, int]
    RemoteWakeup: Union[_t.UCHAR, int]
    PullDownEnable: Union[_t.UCHAR, int]

    @classmethod
    def from_struct(cls, data: c.Structure):
        inst = cls()
        for key in cls.__annotations__:
            inst[key] = getattr(data, key)
        return inst


class ProgramData_X_Series(TypedDict, total=False):
    common: Union[_t.ft_eeprom_header, ProgramData_Common]
    ACSlowSlew: Union[_t.UCHAR, int]
    ACSchmittInput: Union[_t.UCHAR, int]
    ACDriveCurrent: Union[_t.UCHAR, int]
    ADSlowSlew: Union[_t.UCHAR, int]
    ADSchmittInput: Union[_t.UCHAR, int]
    ADDriveCurrent: Union[_t.UCHAR, int]
    Cbus0: Union[_t.UCHAR, int]
    Cbus1: Union[_t.UCHAR, int]
    Cbus2: Union[_t.UCHAR, int]
    Cbus3: Union[_t.UCHAR, int]
    Cbus4: Union[_t.UCHAR, int]
    Cbus5: Union[_t.UCHAR, int]
    Cbus6: Union[_t.UCHAR, int]
    InvertTXD: Union[_t.UCHAR, int]
    InvertRXD: Union[_t.UCHAR, int]
    InvertRTS: Union[_t.UCHAR, int]
    InvertCTS: Union[_t.UCHAR, int]
    InvertDTR: Union[_t.UCHAR, int]
    InvertDSR: Union[_t.UCHAR, int]
    InvertDCD: Union[_t.UCHAR, int]
    InvertRI: Union[_t.UCHAR, int]
    BCDEnable: Union[_t.UCHAR, int]
    BCDForceCbusPWREN: Union[_t.UCHAR, int]
    BCDDisableSleep: Union[_t.UCHAR, int]
    I2CSlaveAddress: Union[_t.WORD, int]
    I2CDeviceId: Union[_t.DWORD, int]
    I2CDisableSchmitt: Union[_t.UCHAR, int]
    FT1248Cpol: Union[_t.UCHAR, int]
    FT1248Lsb: Union[_t.UCHAR, int]
    FT1248FlowControl: Union[_t.UCHAR, int]
    RS485EchoSuppress: Union[_t.UCHAR, int]
    PowerSaveEnable: Union[_t.UCHAR, int]
    DriverType: Union[_t.UCHAR, int]

    @classmethod
    def from_struct(cls, data: c.Structure):
        inst = cls()
        for key in cls.__annotations__:
            inst[key] = getattr(data, key)
        inst["common"] = ProgramData_Common.from_struct(data.common)
        return inst


def call_ft(function: Callable, *args):
    """Call an FTDI function and check the status. Raise exception on error"""
    status = function(*args)
    if status != defines.Status.OK:
        raise DeviceError(status)


def listDevices(flags: int = 0) -> Optional[List[bytes]]:
    """Return a list of serial numbers(default), descriptions or
    locations (Windows only) of the connected FTDI devices depending on value
    of flags"""
    n = _t.DWORD()
    call_ft(_ft.FT_ListDevices, c.byref(n), None, _t.DWORD(defines.LIST_NUMBER_ONLY))
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
        call_ft(_ft.FT_ListDevices, ba, c.byref(n), _t.DWORD(defines.LIST_ALL | flags))
        return [res for res in ba[:devcount]]

    return None


def getLibraryVersion() -> int:
    """Return a long representing library version"""
    m = _t.DWORD()
    call_ft(_ft.FT_GetLibraryVersion, c.byref(m))
    return m.value


def createDeviceInfoList() -> int:
    """Create the internal device info list and return number of entries"""
    m = _t.DWORD()
    call_ft(_ft.FT_CreateDeviceInfoList, c.byref(m))
    return m.value


def getDeviceInfoDetail(devnum: int = 0, update: bool = True) -> DeviceInfoDetail:
    """Get an entry from the internal device info list. Set update to
    False to avoid a slow call to createDeviceInfoList."""
    flags = _t.DWORD()
    typ = _t.DWORD()
    dev_id = _t.DWORD()
    location = _t.DWORD()
    handle = _t.FT_HANDLE()
    name = c.create_string_buffer(defines.MAX_DESCRIPTION_SIZE)
    description = c.create_string_buffer(defines.MAX_DESCRIPTION_SIZE)
    # createDeviceInfoList is slow, only run if update is True
    if update:
        createDeviceInfoList()
    call_ft(
        _ft.FT_GetDeviceInfoDetail,
        _t.DWORD(devnum),
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


def open(dev: int = 0, update: bool = True):  # pylint: disable=redefined-builtin
    """Open a handle to a usb device by index and return an FTD2XX instance for
    it. Set update to False to avoid a slow call to createDeviceInfoList.

    Args:
        dev (int): Device number
        update (bool): Set False to disable automatic call to createDeviceInfoList

    Returns:
        instance of FTD2XX instance if successful
    """
    h = _t.FT_HANDLE()
    call_ft(_ft.FT_Open, dev, c.byref(h))
    return FTD2XX(h, update=update)


def openEx(
    id_str: bytes, flags: int = defines.OPEN_BY_SERIAL_NUMBER, update: bool = True
):
    """Open a handle to a usb device by serial number(default), description or
    location(Windows only) depending on value of flags and return an FTD2XX
    instance for it. Set update to False to avoid a slow call to createDeviceInfoList.

    Args:
        id_str (bytes): ID string from listDevices
        flags (int) = FLAG (consult D2XX Guide). Defaults to OPEN_BY_SERIAL_NUMBER
        update (bool): Set False to disable automatic call to createDeviceInfoList

    Returns:
        instance of FTD2XX instance if successful
    """
    h = _t.FT_HANDLE()
    call_ft(_ft.FT_OpenEx, id_str, _t.DWORD(flags), c.byref(h))
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
                _t.STRING(name),
                _t.DWORD(access),
                _t.DWORD(0),
                None,
                _t.DWORD(OPEN_EXISTING),
                _t.DWORD(flags),
                _t.HANDLE(0),
            )
        )


else:

    def getVIDPID() -> Tuple[int, int]:
        """Linux only. Get the VID and PID of the device"""
        vid = _t.DWORD()
        pid = _t.DWORD()
        call_ft(_ft.FT_GetVIDPID, c.byref(vid), c.byref(pid))
        return (vid.value, pid.value)

    def setVIDPID(vid, pid):
        """Linux only. Set the VID and PID of the device"""
        call_ft(_ft.FT_SetVIDPID, _t.DWORD(vid), _t.DWORD(pid))
        return None


class FTD2XX(AbstractContextManager):
    """Class for communicating with an FTDI device"""

    handle: _t.FT_HANDLE
    status: int
    type: defines.Device

    def __init__(self, handle: _t.FT_HANDLE, update: bool = True):
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
        b_read = _t.DWORD()
        b = c.create_string_buffer(nchars)
        call_ft(_ft.FT_Read, self.handle, b, nchars, c.byref(b_read))
        return b.raw[: b_read.value] if raw else b.value[: b_read.value]

    def write(self, data: bytes):
        """Send the data to the device. Data must be a string representing the
        bytes to be sent"""
        w = _t.DWORD()
        call_ft(_ft.FT_Write, self.handle, data, len(data), c.byref(w))
        return w.value

    def ioctl(self):
        """Not implemented"""
        raise NotImplementedError

    def setBaudRate(self, baud: int) -> None:
        """Set the baud rate"""
        call_ft(_ft.FT_SetBaudRate, self.handle, _t.DWORD(baud))

    def setDivisor(self, div: int):
        """Set the clock divider. The clock will be set to 6e6/(div + 1)."""
        call_ft(_ft.FT_SetDivisor, self.handle, _t.USHORT(div))

    def setDataCharacteristics(self, wordlen: int, stopbits: int, parity: int):
        """Set the data characteristics for UART"""
        call_ft(
            _ft.FT_SetDataCharacteristics,
            self.handle,
            _t.UCHAR(wordlen),
            _t.UCHAR(stopbits),
            _t.UCHAR(parity),
        )

    def setFlowControl(self, flowcontrol: int, xon: int = -1, xoff: int = -1):
        if flowcontrol == defines.FLOW_XON_XOFF and (xon == -1 or xoff == -1):
            raise ValueError
        call_ft(
            _ft.FT_SetFlowControl,
            self.handle,
            _t.USHORT(flowcontrol),
            _t.UCHAR(xon),
            _t.UCHAR(xoff),
        )

    def resetDevice(self):
        """Reset the device"""
        call_ft(_ft.FT_ResetDevice, self.handle)

    def setDtr(self):
        call_ft(_ft.FT_SetDtr, self.handle)

    def clrDtr(self):
        call_ft(_ft.FT_ClrDtr, self.handle)

    def setRts(self):
        call_ft(_ft.FT_SetRts, self.handle)

    def clrRts(self):
        call_ft(_ft.FT_ClrRts, self.handle)

    def getModemStatus(self) -> defines.ModemStatus:
        m = _t.DWORD()
        call_ft(_ft.FT_GetModemStatus, self.handle, c.byref(m))
        return defines.ModemStatus(m.value & 0xFFFF)

    def setChars(self, evch: int, evch_en: int, erch: int, erch_en: int):
        call_ft(
            _ft.FT_SetChars,
            self.handle,
            _t.UCHAR(evch),
            _t.UCHAR(evch_en),
            _t.UCHAR(erch),
            _t.UCHAR(erch_en),
        )

    def purge(self, mask: int = 0):
        if not mask:
            mask = defines.PURGE_RX | defines.PURGE_TX
        call_ft(_ft.FT_Purge, self.handle, _t.DWORD(mask))

    def setTimeouts(self, read: int, write: int):
        call_ft(_ft.FT_SetTimeouts, self.handle, _t.DWORD(read), _t.DWORD(write))

    def setDeadmanTimeout(self, timeout: int):
        call_ft(_ft.FT_SetDeadmanTimeout, self.handle, _t.DWORD(timeout))

    def getQueueStatus(self) -> int:
        """Get number of bytes in receive queue."""
        rxQAmount = _t.DWORD()
        call_ft(_ft.FT_GetQueueStatus, self.handle, c.byref(rxQAmount))
        return rxQAmount.value

    def setEventNotification(self, evtmask: int, evthandle):
        call_ft(
            _ft.FT_SetEventNotification,
            self.handle,
            _t.DWORD(evtmask),
            _t.HANDLE(evthandle),
        )

    def getStatus(self):
        """Return a 3-tuple of rx queue bytes, tx queue bytes and event
        status"""
        rxQAmount = _t.DWORD()
        txQAmount = _t.DWORD()
        evtStatus = _t.DWORD()
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
        call_ft(_ft.FT_SetWaitMask, self.handle, _t.DWORD(mask))

    def waitOnMask(self):
        mask = _t.DWORD()
        call_ft(_ft.FT_WaitOnMask, self.handle, c.byref(mask))
        return mask.value

    def getEventStatus(self):
        evtStatus = _t.DWORD()
        call_ft(_ft.FT_GetEventStatus, self.handle, c.byref(evtStatus))
        return evtStatus.value

    def setLatencyTimer(self, latency: int):
        call_ft(_ft.FT_SetLatencyTimer, self.handle, _t.UCHAR(latency))

    def getLatencyTimer(self) -> int:
        latency = _t.UCHAR()
        call_ft(_ft.FT_GetLatencyTimer, self.handle, c.byref(latency))
        return latency.value

    def setBitMode(self, mask: int, enable: bool):
        call_ft(_ft.FT_SetBitMode, self.handle, _t.UCHAR(mask), _t.UCHAR(enable))

    def getBitMode(self) -> int:
        mask = _t.UCHAR()
        call_ft(_ft.FT_GetBitMode, self.handle, c.byref(mask))
        return mask.value

    def setUSBParameters(self, in_tx_size: int, out_tx_size: int = 0):
        call_ft(
            _ft.FT_SetUSBParameters,
            self.handle,
            _t.ULONG(in_tx_size),
            _t.ULONG(out_tx_size),
        )

    def getDeviceInfo(self) -> DeviceInfo:
        """Returns a dictionary describing the device."""
        deviceType = _t.DWORD()
        deviceId = _t.DWORD()
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
        call_ft(_ft.FT_SetResetPipeRetryCount, self.handle, _t.DWORD(count))

    def resetPort(self):
        call_ft(_ft.FT_ResetPort, self.handle)

    def cyclePort(self):
        call_ft(_ft.FT_CyclePort, self.handle)

    def getDriverVersion(self) -> int:
        drvver = _t.DWORD()
        call_ft(_ft.FT_GetDriverVersion, self.handle, c.byref(drvver))
        return drvver.value

    def getComPortNumber(self) -> int:
        """Return a long representing the COM port number"""
        m = _t.LONG()
        try:
            call_ft(_ft.FT_GetComPortNumber, self.handle, c.byref(m))
        except AttributeError as exc:
            raise Exception("FT_GetComPortNumber is only available on windows") from exc
        return m.value

    def eeProgram(self, progdata: Optional[ft_program_data] = None, **kwds) -> None:
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
        progdata.Signature1 = _t.DWORD(0)
        progdata.Signature2 = _t.DWORD(0xFFFFFFFF)
        progdata.Version = _t.DWORD(2)
        call_ft(_ft.FT_EE_Program, self.handle, progdata)

    def eeRead(self) -> ft_program_data:
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
            Signature1=0,
            Signature2=0xFFFFFFFF,
            Version=2,
            Manufacturer=c.cast(Manufacturer, _t.STRING),
            ManufacturerId=c.cast(ManufacturerId, _t.STRING),
            Description=c.cast(Description, _t.STRING),
            SerialNumber=c.cast(SerialNumber, _t.STRING),
        )

        call_ft(_ft.FT_EE_Read, self.handle, c.byref(progdata))
        return ProgramData.from_struct(progdata)

    def eeUASize(self) -> int:
        """Get the EEPROM user area size"""
        uasize = _t.DWORD()
        call_ft(_ft.FT_EE_UASize, self.handle, c.byref(uasize))
        return uasize.value

    def eeUAWrite(self, data: bytes) -> None:
        """Write data to the EEPROM user area. data must be a string with
        appropriate byte values"""
        buf = c.create_string_buffer(data)
        call_ft(_ft.FT_EE_UAWrite, self.handle, buf, len(data))

    def eeUARead(self, b_to_read: int) -> bytes:
        """Read b_to_read bytes from the EEPROM user area"""
        b_read = _t.DWORD()
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

    def eepromRead(self):
        """Get the program information from the EEPROM"""
        #        if self.devInfo['type'] == 4:
        #            version = 1
        #        elif self.devInfo['type'] == 5:
        #            version = 2
        #        else:
        #            version = 0
        if self.type == defines.Device.FT_X_SERIES:
            progdata = _t.ft_eeprom_x_series()
        else:
            raise DeviceError("Only X series support is implemented! Sorry.")
        progdata.common = _t.ft_eeprom_header(deviceType=self.type)

        Manufacturer = c.create_string_buffer(defines.MAX_DESCRIPTION_SIZE)
        ManufacturerId = c.create_string_buffer(defines.MAX_DESCRIPTION_SIZE)
        Description = c.create_string_buffer(defines.MAX_DESCRIPTION_SIZE)
        SerialNumber = c.create_string_buffer(defines.MAX_DESCRIPTION_SIZE)

        call_ft(
            _ft.FT_EEPROM_Read,
            self.handle,
            c.byref(progdata),
            _t.DWORD(c.sizeof(progdata)),
            c.cast(Manufacturer, _t.STRING),
            c.cast(ManufacturerId, _t.STRING),
            c.cast(Description, _t.STRING),
            c.cast(SerialNumber, _t.STRING),
        )
        return (
            ProgramData_X_Series.from_struct(progdata),
            Manufacturer.value,
            ManufacturerId.value,
            Description.value,
            SerialNumber.value,
        )

    def __exit__(
        self,
        __exc_type: Optional[Type[BaseException]],
        __exc_value: Optional[BaseException],
        __traceback: Optional[TracebackType],
    ) -> Optional[bool]:
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
