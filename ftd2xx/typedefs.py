import sys
from ctypes import (
    POINTER,
    Structure,
    c_char_p,
    c_ubyte,
    c_void_p,
    c_char,
    c_int,
    c_ulong,
    c_ulonglong,
)

CHAR = c_char
INT = c_int
STRING = c_char_p
LPTSTR = STRING
UCHAR = c_ubyte
PVOID = c_void_p
PUCHAR = POINTER(c_ubyte)
ULONGLONG = c_ulonglong

if sys.platform == "win32":
    from ctypes.wintypes import (
        BOOL,
        BYTE,
        USHORT,
        WORD,
        DWORD,
        LONG,
        ULONG,
        HANDLE,
        PCHAR,
        PULONG,
        LPVOID,
        LPCSTR,
        LPWORD,
        LPLONG,
    )

    LPDWORD = POINTER(DWORD)

elif sys.platform.startswith("linux") or sys.platform == "darwin":
    from ctypes import c_short, c_ushort, c_long

    BOOL = c_int
    BYTE = c_ubyte
    SHORT = c_short
    USHORT = c_ushort
    WORD = c_ushort
    DWORD = c_ulong
    LONG = c_long
    ULONG = c_ulong
    HANDLE = c_void_p
    PCHAR = STRING
    LPVOID = PVOID
    LPCSTR = STRING
else:
    raise Exception("Unknown platform")

FT_HANDLE = POINTER(DWORD)
FT_STATUS = ULONG
FT_DEVICE = ULONG


class OVERLAPPED(Structure):
    _fields_ = [
        # WinTypes.h 38
        ("Internal", DWORD),
        ("InternalHigh", DWORD),
        ("Offset", DWORD),
        ("OffsetHigh", DWORD),
        ("hEvent", HANDLE),
    ]


LPOVERLAPPED = POINTER(OVERLAPPED)


class SECURITY_ATTRIBUTES(Structure):
    _fields_ = [
        # WinTypes.h 46
        ("nLength", DWORD),
        ("lpSecurityDescriptor", LPVOID),
        ("bInheritHandle", BOOL),
    ]


LPSECURITY_ATTRIBUTES = POINTER(SECURITY_ATTRIBUTES)


class ft_eeprom_header(Structure):
    _fields_ = [
        ("deviceType", FT_DEVICE),  # FTxxxx device type to be programmed
        # Device descriptor options
        ("VendorId", WORD),  # 0x0403
        ("ProductId", WORD),  # 0x6001
        ("SerNumEnable", UCHAR),  # non-zero if serial number to be used
        # Config descriptor options
        ("MaxPower", WORD),  # 0 < MaxPower <= 500
        ("SelfPowered", UCHAR),  # 0 = bus powered, 1 = self powered
        ("RemoteWakeup", UCHAR),  # 0 = not capable, 1 = capable
        # Hardware options
        ("PullDownEnable", UCHAR),  # non-zero if pull down in suspend enabled
    ]


class ft_eeprom_232b(Structure):
    _fields_ = [
        # Common header
        ("common", ft_eeprom_header)  # common elements for all device EEPROMs
    ]


class ft_eeprom_2232(Structure):
    _fields_ = [
        # Common header
        ("common", ft_eeprom_header),  # common elements for all device EEPROMs
        # Drive options
        ("AIsHighCurrent", UCHAR),  # non-zero if interface is high current
        ("BIsHighCurrent", UCHAR),  # non-zero if interface is high current
        # Hardware options
        ("AIsFifo", UCHAR),  # non-zero if interface is 245 FIFO
        ("AIsFifoTar", UCHAR),  # non-zero if interface is 245 FIFO CPU target
        ("AIsFastSer", UCHAR),  # non-zero if interface is Fast serial
        ("BIsFifo", UCHAR),  # non-zero if interface is 245 FIFO
        ("BIsFifoTar", UCHAR),  # non-zero if interface is 245 FIFO CPU target
        ("BIsFastSer", UCHAR),  # non-zero if interface is Fast serial
        # Driver option
        ("ADriverType", UCHAR),  #
        ("BDriverType", UCHAR),  #
    ]


class ft_eeprom_232r(Structure):
    _fields_ = [
        # Common header
        ("common", ft_eeprom_header),  # common elements for all device EEPROMs
        # Drive options
        ("IsHighCurrent", UCHAR),  # non-zero if interface is high current
        # Hardware options
        ("UseExtOsc", UCHAR),  # Use External Oscillator
        ("InvertTXD", UCHAR),  # non-zero if invert TXD
        ("InvertRXD", UCHAR),  # non-zero if invert RXD
        ("InvertRTS", UCHAR),  # non-zero if invert RTS
        ("InvertCTS", UCHAR),  # non-zero if invert CTS
        ("InvertDTR", UCHAR),  # non-zero if invert DTR
        ("InvertDSR", UCHAR),  # non-zero if invert DSR
        ("InvertDCD", UCHAR),  # non-zero if invert DCD
        ("InvertRI", UCHAR),  # non-zero if invert RI
        ("Cbus0", UCHAR),  # Cbus Mux control
        ("Cbus1", UCHAR),  # Cbus Mux control
        ("Cbus2", UCHAR),  # Cbus Mux control
        ("Cbus3", UCHAR),  # Cbus Mux control
        ("Cbus4", UCHAR),  # Cbus Mux control
        # Driver option
        ("DriverType", UCHAR),
    ]


class ft_eeprom_2232h(Structure):
    _fields_ = [
        # Common header
        ("common", ft_eeprom_header),  # common elements for all device EEPROMs
        # Drive options
        ("ALSlowSlew", UCHAR),  # non-zero if AL pins have slow slew
        ("ALSchmittInput", UCHAR),  # non-zero if AL pins are Schmitt input
        ("ALDriveCurrent", UCHAR),  # valid values are 4mA, 8mA, 12mA, 16mA
        ("AHSlowSlew", UCHAR),  # non-zero if AH pins have slow slew
        ("AHSchmittInput", UCHAR),  # non-zero if AH pins are Schmitt input
        ("AHDriveCurrent", UCHAR),  # valid values are 4mA, 8mA, 12mA, 16mA
        ("BLSlowSlew", UCHAR),  # non-zero if BL pins have slow slew
        ("BLSchmittInput", UCHAR),  # non-zero if BL pins are Schmitt input
        ("BLDriveCurrent", UCHAR),  # valid values are 4mA, 8mA, 12mA, 16mA
        ("BHSlowSlew", UCHAR),  # non-zero if BH pins have slow slew
        ("BHSchmittInput", UCHAR),  # non-zero if BH pins are Schmitt input
        ("BHDriveCurrent", UCHAR),  # valid values are 4mA, 8mA, 12mA, 16mA
        # Hardware options
        ("AIsFifo", UCHAR),  # non-zero if interface is 245 FIFO
        ("AIsFifoTar", UCHAR),  # non-zero if interface is 245 FIFO CPU target
        ("AIsFastSer", UCHAR),  # non-zero if interface is Fast serial
        ("BIsFifo", UCHAR),  # non-zero if interface is 245 FIFO
        ("BIsFifoTar", UCHAR),  # non-zero if interface is 245 FIFO CPU target
        ("BIsFastSer", UCHAR),  # non-zero if interface is Fast serial
        ("PowerSaveEnable", UCHAR),  # non-zero if using BCBUS7 to save power for
        # self-powered designs
        # Driver option
        ("ADriverType", UCHAR),  #
        ("BDriverType", UCHAR),  #
    ]


class ft_eeprom_4232h(Structure):
    _fields_ = [
        # Common header
        ("common", ft_eeprom_header),  # common elements for all device EEPROMs
        # Drive options
        ("ASlowSlew", UCHAR),  # non-zero if A pins have slow slew
        ("ASchmittInput", UCHAR),  # non-zero if A pins are Schmitt input
        ("ADriveCurrent", UCHAR),  # valid values are 4mA, 8mA, 12mA, 16mA
        ("BSlowSlew", UCHAR),  # non-zero if B pins have slow slew
        ("BSchmittInput", UCHAR),  # non-zero if B pins are Schmitt input
        ("BDriveCurrent", UCHAR),  # valid values are 4mA, 8mA, 12mA, 16mA
        ("CSlowSlew", UCHAR),  # non-zero if C pins have slow slew
        ("CSchmittInput", UCHAR),  # non-zero if C pins are Schmitt input
        ("CDriveCurrent", UCHAR),  # valid values are 4mA, 8mA, 12mA, 16mA
        ("DSlowSlew", UCHAR),  # non-zero if D pins have slow slew
        ("DSchmittInput", UCHAR),  # non-zero if D pins are Schmitt input
        ("DDriveCurrent", UCHAR),  # valid values are 4mA, 8mA, 12mA, 16mA
        # Hardware options
        ("ARIIsTXDEN", UCHAR),  # non-zero if port A uses RI as RS485 TXDEN
        ("BRIIsTXDEN", UCHAR),  # non-zero if port B uses RI as RS485 TXDEN
        ("CRIIsTXDEN", UCHAR),  # non-zero if port C uses RI as RS485 TXDEN
        ("DRIIsTXDEN", UCHAR),  # non-zero if port D uses RI as RS485 TXDEN
        # Driver option
        ("ADriverType", UCHAR),  #
        ("BDriverType", UCHAR),  #
        ("CDriverType", UCHAR),  #
        ("DDriverType", UCHAR),  #
    ]


class ft_eeprom_232h(Structure):
    _fields_ = [
        # Common header
        ("common", ft_eeprom_header),  # common elements for all device EEPROMs
        # Drive options
        ("ACSlowSlew", UCHAR),  # non-zero if AC bus pins have slow slew
        ("ACSchmittInput", UCHAR),  # non-zero if AC bus pins are Schmitt input
        ("ACDriveCurrent", UCHAR),  # valid values are 4mA, 8mA, 12mA, 16mA
        ("ADSlowSlew", UCHAR),  # non-zero if AD bus pins have slow slew
        ("ADSchmittInput", UCHAR),  # non-zero if AD bus pins are Schmitt input
        ("ADDriveCurrent", UCHAR),  # valid values are 4mA, 8mA, 12mA, 16mA
        # CBUS Options
        ("Cbus0", UCHAR),  # Cbus Mux control
        ("Cbus1", UCHAR),  # Cbus Mux control
        ("Cbus2", UCHAR),  # Cbus Mux control
        ("Cbus3", UCHAR),  # Cbus Mux control
        ("Cbus4", UCHAR),  # Cbus Mux control
        ("Cbus5", UCHAR),  # Cbus Mux control
        ("Cbus6", UCHAR),  # Cbus Mux control
        ("Cbus7", UCHAR),  # Cbus Mux control
        ("Cbus8", UCHAR),  # Cbus Mux control
        ("Cbus9", UCHAR),  # Cbus Mux control
        # FT1248 options
        (
            "FT1248Cpol",
            UCHAR,
        ),  # FT1248 clock polarity - clock idle high (1) or clock idle low (0)
        ("FT1248Lsb", UCHAR),  # FT1248 data is LSB (1) or MSB (0)
        ("FT1248FlowControl", UCHAR),  # FT1248 flow control enable
        # Hardware options
        ("IsFifo", UCHAR),  # non-zero if interface is 245 FIFO
        ("IsFifoTar", UCHAR),  # non-zero if interface is 245 FIFO CPU target
        ("IsFastSer", UCHAR),  # non-zero if interface is Fast serial
        ("IsFT1248", UCHAR),  # non-zero if interface is FT1248
        ("PowerSaveEnable", UCHAR),
        # Driver option
        ("DriverType", UCHAR),
    ]


class ft_eeprom_x_series(Structure):
    _fields_ = [
        # Common header
        ("common", ft_eeprom_header),  # common elements for all device EEPROMs
        # Drive options
        ("ACSlowSlew", UCHAR),  # non-zero if AC bus pins have slow slew
        ("ACSchmittInput", UCHAR),  # non-zero if AC bus pins are Schmitt input
        ("ACDriveCurrent", UCHAR),  # valid values are 4mA, 8mA, 12mA, 16mA
        ("ADSlowSlew", UCHAR),  # non-zero if AD bus pins have slow slew
        ("ADSchmittInput", UCHAR),  # non-zero if AD bus pins are Schmitt input
        ("ADDriveCurrent", UCHAR),  # valid values are 4mA, 8mA, 12mA, 16mA
        # CBUS options
        ("Cbus0", UCHAR),  # Cbus Mux control
        ("Cbus1", UCHAR),  # Cbus Mux control
        ("Cbus2", UCHAR),  # Cbus Mux control
        ("Cbus3", UCHAR),  # Cbus Mux control
        ("Cbus4", UCHAR),  # Cbus Mux control
        ("Cbus5", UCHAR),  # Cbus Mux control
        ("Cbus6", UCHAR),  # Cbus Mux control
        # UART signal options
        ("InvertTXD", UCHAR),  # non-zero if invert TXD
        ("InvertRXD", UCHAR),  # non-zero if invert RXD
        ("InvertRTS", UCHAR),  # non-zero if invert RTS
        ("InvertCTS", UCHAR),  # non-zero if invert CTS
        ("InvertDTR", UCHAR),  # non-zero if invert DTR
        ("InvertDSR", UCHAR),  # non-zero if invert DSR
        ("InvertDCD", UCHAR),  # non-zero if invert DCD
        ("InvertRI", UCHAR),  # non-zero if invert RI
        # Battery Charge Detect options
        ("BCDEnable", UCHAR),  # Enable Battery Charger Detection
        (
            "BCDForceCbusPWREN",
            UCHAR,
        ),  # asserts the power enable signal on CBUS when charging port detected
        ("BCDDisableSleep", UCHAR),  # forces the device never to go into sleep mode
        # I2C options
        ("I2CSlaveAddress", WORD),  # I2C slave device address
        ("I2CDeviceId", DWORD),  # I2C device ID
        ("I2CDisableSchmitt", UCHAR),  # Disable I2C Schmitt trigger
        # FT1248 options
        (
            "FT1248Cpol",
            UCHAR,
        ),  # FT1248 clock polarity - clock idle high (1) or clock idle low(0)
        ("FT1248Lsb", UCHAR),  # FT1248 data is LSB (1) or MSB (0)
        ("FT1248FlowControl", UCHAR),  # FT1248 flow control enable
        # Hardware options
        ("RS485EchoSuppress", UCHAR),
        ("PowerSaveEnable", UCHAR),
        # Driver option
        ("DriverType", UCHAR),
    ]


class StructureWithDefaults(Structure):
    def __init__(self, **kwargs):
        """
        Ctypes.Structure with integrated default values.

        :param kwargs: values different to defaults
        :type kwargs: dict
        """

        values = type(self)._defaults_.copy()  # type: ignore
        values.update(kwargs)

        super().__init__(**values)  # Python 3 syntax


class FTDCB(StructureWithDefaults):
    _fields_ = [
        ("DCBlength", DWORD),  # sizeof(FTDCB)
        ("BaudRate", DWORD),  # Baud rate at which running
        ("fBinary", DWORD, 1),  # Binary Mode (skip EOF check)
        ("fParity", DWORD, 1),  # Enable parity checking
        ("fOutxCtsFlow", DWORD, 1),  # CTS handshaking on output
        ("fOutxDsrFlow", DWORD, 1),  # DSR handshaking on output
        ("fDtrControl", DWORD, 2),  # DTR Flow control
        ("fDsrSensitivity", DWORD, 1),  # DSR Sensitivity
        ("fTXContinueOnXoff", DWORD, 1),  # Continue TX when Xoff sent
        ("fOutX", DWORD, 1),  # Enable output X-ON/X-OFF
        ("fInX", DWORD, 1),  # Enable input X-ON/X-OFF
        ("fErrorChar", DWORD, 1),  # Enable Err Replacement
        ("fNull", DWORD, 1),  # Enable Null stripping
        ("fRtsControl", DWORD, 2),  # Rts Flow control
        ("fAbortOnError", DWORD, 1),  # Abort all reads and writes on Error
        ("fDummy2", DWORD, 17),  # Reserved
        ("wReserved", WORD),  # Not currently used
        ("XonLim", WORD),  # Transmit X-ON threshold
        ("XoffLim", WORD),  # Transmit X-OFF threshold
        ("ByteSize", BYTE),  # Number of bits/byte, 7-8
        ("Parity", BYTE),  # 0-4=None,Odd,Even,Mark,Space
        ("StopBits", BYTE),  # 0,2 = 1, 2
        ("XonChar", CHAR),  # Tx and Rx X-ON character
        ("XoffChar", CHAR),  # Tx and Rx X-OFF character
        ("ErrorChar", CHAR),  # Error replacement char
        ("EofChar", CHAR),  # End of Input character
        ("EvtChar", CHAR),  # Received Event character
        ("wReserved1", WORD),  # Fill
    ]

    _defaults_ = {
        "fBinary": 1,
        "fParity": 1,
        "fOutxCtsFlow": 1,
        "fOutxDsrFlow": 1,
        "fDtrControl": 2,
        "fDsrSensitivity": 1,
        "fTXContinueOnXoff": 1,
        "fOutX": 1,
        "fInX": 1,
        "fErrorChar": 1,
        "fNull": 1,
        "fRtsControl": 2,
        "fAbortOnError": 1,
        "fDummy2": 17,
    }


LPFTDCB = POINTER(FTDCB)


class FTTIMEOUTS(Structure):
    _fields_ = [
        ("ReadIntervalTimeout", DWORD),  # Maximum time between read chars
        ("ReadTotalTimeoutMultiplier", DWORD),  # Multiplier of characters
        ("ReadTotalTimeoutConstant", DWORD),  # Constant in milliseconds
        ("WriteTotalTimeoutMultiplier", DWORD),  # Multiplier of characters
        ("WriteTotalTimeoutConstant", DWORD),  # Constant in milliseconds
    ]


# LPFTTIMEOUTS = POINTER(FTTIMEOUTS)


class FTCOMSTAT(StructureWithDefaults):
    _fields_ = [
        ("fCtsHold", DWORD, 1),
        ("fDsrHold", DWORD, 1),
        ("fRlsdHold", DWORD, 1),
        ("fXoffHold", DWORD, 1),
        ("fXoffSent", DWORD, 1),
        ("fEof", DWORD, 1),
        ("fTxim", DWORD, 1),
        ("fReserved", DWORD, 25),
        ("cbInQue", DWORD),
        ("cbOutQue", DWORD),
    ]

    _defaults_ = {
        "fCtsHold": 1,
        "fDsrHold": 1,
        "fRlsdHold": 1,
        "fXoffHold": 1,
        "fXoffSent": 1,
        "fEof": 1,
        "fTxim": 1,
        "fReserved": 25,
    }


LPFTCOMSTAT = POINTER(FTCOMSTAT)


class ft_program_data(Structure):
    _fields_ = [
        ("Signature1", DWORD),  # Header - must be 0x0000000
        ("Signature2", DWORD),  # Header - must be 0xFFFFFFFF
        # Header - FT_PROGRAM_DATA version
        # 0 = original (FT232B)
        # 1 = FT2232 extensions
        # 2 = FT232R extensions
        # 3 = FT2232H extensions
        # 4 = FT4232H extensions
        # 5 = FT232H extensions
        ("Version", DWORD),
        ("VendorId", WORD),  # 0x0403
        ("ProductId", WORD),  # 0x6001
        ("Manufacturer", STRING),  # "FTDI"
        ("ManufacturerId", STRING),  # "FT"
        ("Description", STRING),  # "USB HS Serial Converter"
        ("SerialNumber", STRING),  # FT000001" if fixed, or NULL
        ("MaxPower", WORD),  # 0 < MaxPower <= 500
        ("PnP", WORD),  # 0 = disabled, 1 = enabled
        ("SelfPowered", WORD),  # 0 = bus powered, 1 = self powered
        ("RemoteWakeup", WORD),  # 0 = not capable, 1 = capable
        #
        # Rev4 (FT232B) extensions
        #
        ("Rev4", UCHAR),  # non-zero if Rev4 chip, zero otherwise
        ("IsoIn", UCHAR),  # non-zero if in endpoint is isochronous
        ("IsoOut", UCHAR),  # non-zero if out endpoint is isochronous
        ("PullDownEnable", UCHAR),  # non-zero if pull down enabled
        ("SerNumEnable", UCHAR),  # non-zero if serial number to be used
        ("USBVersionEnable", UCHAR),  # non-zero if chip uses USBVersion
        ("USBVersion", WORD),  # BCD (0x0200 => USB2)
        #
        # Rev 5 (FT2232) extensions
        #
        ("Rev5", UCHAR),  # non-zero if Rev5 chip, zero otherwise
        ("IsoInA", UCHAR),  # non-zero if in endpoint is isochronous
        ("IsoInB", UCHAR),  # non-zero if in endpoint is isochronous
        ("IsoOutA", UCHAR),  # on-zero if out endpoint is isochronous
        ("IsoOutB", UCHAR),  # non-zero if out endpoint is isochronous
        ("PullDownEnable5", UCHAR),  # non-zero if pull down enabled
        ("SerNumEnable5", UCHAR),  # non-zero if serial number to be used
        ("USBVersionEnable5", UCHAR),  # non-zero if chip uses USBVersion
        ("USBVersion5", WORD),  # BCD (0x0200 => USB2)
        ("AIsHighCurrent", UCHAR),  # non-zero if interface is high current
        ("BIsHighCurrent", UCHAR),  # non-zero if interface is high current
        ("IFAIsFifo", UCHAR),  # non-zero if interface is 245 FIFO
        ("IFAIsFifoTar", UCHAR),  # non-zero if interface is 245 FIFO CPU target
        ("IFAIsFastSer", UCHAR),  # non-zero if interface is Fast serial
        ("AIsVCP", UCHAR),  # non-zero if interface is to use VCP drivers
        ("IFBIsFifo", UCHAR),  # non-zero if interface is 245 FIFO
        ("IFBIsFifoTar", UCHAR),  # non-zero if interface is 245 FIFO CPU target
        ("IFBIsFastSer", UCHAR),  # non-zero if interface is Fast serial
        ("BIsVCP", UCHAR),  # non-zero if interface is to use VCP drivers
        #
        # Rev 6 (FT232R) extensions
        #
        ("UseExtOsc", UCHAR),  # Use External Oscillator
        ("HighDriveIOs", UCHAR),  # High Drive I/Os
        ("EndpointSize", UCHAR),  # Endpoint size
        ("PullDownEnableR", UCHAR),  # non-zero if pull down enabled
        ("SerNumEnableR", UCHAR),  # non-zero if serial number to be used
        ("InvertTXD", UCHAR),  # non-zero if invert TXD
        ("InvertRXD", UCHAR),  # non-zero if invert RXD
        ("InvertRTS", UCHAR),  # non-zero if invert RTS
        ("InvertCTS", UCHAR),  # non-zero if invert CTS
        ("InvertDTR", UCHAR),  # non-zero if invert DTR
        ("InvertDSR", UCHAR),  # non-zero if invert DSR
        ("InvertDCD", UCHAR),  # non-zero if invert DCD
        ("InvertRI", UCHAR),  # non-zero if invert RI
        ("Cbus0", UCHAR),  # Cbus Mux control
        ("Cbus1", UCHAR),  # Cbus Mux control
        ("Cbus2", UCHAR),  # Cbus Mux control
        ("Cbus3", UCHAR),  # Cbus Mux control
        ("Cbus4", UCHAR),  # Cbus Mux control
        ("RIsD2XX", UCHAR),  # non-zero if using D2XX driver
        #
        # Rev 7 (FT2232H) Extensions
        #
        ("PullDownEnable7", UCHAR),  # non-zero if pull down enabled
        ("SerNumEnable7", UCHAR),  # non-zero if serial number to be used
        ("ALSlowSlew", UCHAR),  # non-zero if AL pins have slow slew
        ("ALSchmittInput", UCHAR),  # non-zero if AL pins are Schmitt input
        ("ALDriveCurrent", UCHAR),  # valid values are 4mA, 8mA, 12mA, 16mA
        ("AHSlowSlew", UCHAR),  # non-zero if AH pins have slow slew
        ("AHSchmittInput", UCHAR),  # non-zero if AH pins are Schmitt input
        ("AHDriveCurrent", UCHAR),  # valid values are 4mA, 8mA, 12mA, 16mA
        ("BLSlowSlew", UCHAR),  # non-zero if BL pins have slow slew
        ("BLSchmittInput", UCHAR),  # non-zero if BL pins are Schmitt input
        ("BLDriveCurrent", UCHAR),  # valid values are 4mA, 8mA, 12mA, 16mA
        ("BHSlowSlew", UCHAR),  # non-zero if BH pins have slow slew
        ("BHSchmittInput", UCHAR),  # non-zero if BH pins are Schmitt input
        ("BHDriveCurrent", UCHAR),  # valid values are 4mA, 8mA, 12mA, 16mA
        ("IFAIsFifo7", UCHAR),  # non-zero if interface is 245 FIFO
        ("IFAIsFifoTar7", UCHAR),  # non-zero if interface is 245 FIFO CPU target
        ("IFAIsFastSer7", UCHAR),  # non-zero if interface is Fast serial
        ("AIsVCP7", UCHAR),  # non-zero if interface is to use VCP drivers
        ("IFBIsFifo7", UCHAR),  # non-zero if interface is 245 FIFO
        ("IFBIsFifoTar7", UCHAR),  # non-zero if interface is 245 FIFO CPU target
        ("IFBIsFastSer7", UCHAR),  # non-zero if interface is Fast serial
        ("BIsVCP7", UCHAR),  # non-zero if interface is to use VCP drivers
        # non-zero if using BCBUS7 to save power for self-powered designs
        ("PowerSaveEnable", UCHAR),
        #
        # Rev 8 (FT4232H) Extensions
        #
        ("PullDownEnable8", UCHAR),  # non-zero if pull down enabled
        ("SerNumEnable8", UCHAR),  # non-zero if serial number to be used
        ("ASlowSlew", UCHAR),  # non-zero if A pins have slow slew
        ("ASchmittInput", UCHAR),  # non-zero if A pins are Schmitt input
        ("ADriveCurrent", UCHAR),  # valid values are 4mA, 8mA, 12mA, 16mA
        ("BSlowSlew", UCHAR),  # non-zero if B pins have slow slew
        ("BSchmittInput", UCHAR),  # non-zero if B pins are Schmitt input
        ("BDriveCurrent", UCHAR),  # valid values are 4mA, 8mA, 12mA, 16mA
        ("CSlowSlew", UCHAR),  # non-zero if C pins have slow slew
        ("CSchmittInput", UCHAR),  # non-zero if C pins are Schmitt input
        ("CDriveCurrent", UCHAR),  # valid values are 4mA, 8mA, 12mA, 16mA
        ("DSlowSlew", UCHAR),  # non-zero if D pins have slow slew
        ("DSchmittInput", UCHAR),  # non-zero if D pins are Schmitt input
        ("DDriveCurrent", UCHAR),  # valid values are 4mA, 8mA, 12mA, 16mA
        ("ARIIsTXDEN", UCHAR),  # non-zero if port A uses RI as RS485 TXDEN
        ("BRIIsTXDEN", UCHAR),  # non-zero if port B uses RI as RS485 TXDEN
        ("CRIIsTXDEN", UCHAR),  # non-zero if port C uses RI as RS485 TXDEN
        ("DRIIsTXDEN", UCHAR),  # non-zero if port D uses RI as RS485 TXDEN
        ("AIsVCP8", UCHAR),  # non-zero if interface is to use VCP drivers
        ("BIsVCP8", UCHAR),  # non-zero if interface is to use VCP drivers
        ("CIsVCP8", UCHAR),  # non-zero if interface is to use VCP drivers
        ("DIsVCP8", UCHAR),  # non-zero if interface is to use VCP drivers
        #
        # Rev 9 (FT232H) Extensions
        #
        ("PullDownEnableH", UCHAR),  # non-zero if pull down enabled
        ("SerNumEnableH", UCHAR),  # non-zero if serial number to be used
        ("ACSlowSlewH", UCHAR),  # non-zero if AC pins have slow slew
        ("ACSchmittInputH", UCHAR),  # non-zero if AC pins are Schmitt input
        ("ACDriveCurrentH", UCHAR),  # valid values are 4mA, 8mA, 12mA, 16mA
        ("ADSlowSlewH", UCHAR),  # non-zero if AD pins have slow slew
        ("ADSchmittInputH", UCHAR),  # non-zero if AD pins are Schmitt input
        ("ADDriveCurrentH", UCHAR),  # valid values are 4mA, 8mA, 12mA, 16mA
        ("Cbus0H", UCHAR),  # Cbus Mux control
        ("Cbus1H", UCHAR),  # Cbus Mux control
        ("Cbus2H", UCHAR),  # Cbus Mux control
        ("Cbus3H", UCHAR),  # Cbus Mux control
        ("Cbus4H", UCHAR),  # Cbus Mux control
        ("Cbus5H", UCHAR),  # Cbus Mux control
        ("Cbus6H", UCHAR),  # Cbus Mux control
        ("Cbus7H", UCHAR),  # Cbus Mux control
        ("Cbus8H", UCHAR),  # Cbus Mux control
        ("Cbus9H", UCHAR),  # Cbus Mux control
        ("IsFifoH", UCHAR),  # non-zero if interface is 245 FIFO
        ("IsFifoTarH", UCHAR),  # non-zero if interface is 245 FIFO CPU target
        ("IsFastSerH", UCHAR),  # non-zero if interface is Fast serial
        ("IsFT1248H", UCHAR),  # non-zero if interface is FT1248
        # FT1248 clock polarity - clock idle high (1) or clock idle low (0)
        ("FT1248CpolH", UCHAR),
        ("FT1248LsbH", UCHAR),  # FT1248 data is LSB (1) or MSB (0)
        ("FT1248FlowControlH", UCHAR),  # FT1248 flow control enable
        ("IsVCPH", UCHAR),  # non-zero if interface is to use VCP drivers
        # non-zero if using ACBUS7 to save power for self-powered designs
        ("PowerSaveEnableH", UCHAR),
    ]


PFT_PROGRAM_DATA = POINTER(ft_program_data)


class FT_DEVICE_LIST_INFO_NODE(Structure):
    _fields_ = [
        # ftd2xx.h 822
        ("Flags", ULONG),
        ("Type", ULONG),
        ("ID", ULONG),
        ("LocId", DWORD),
        ("SerialNumber", CHAR * 16),
        ("Description", CHAR * 64),
        ("ftHandle", FT_HANDLE),
    ]


__all__ = [
    "FT_HANDLE",
    "FT_STATUS",
    "FT_DEVICE",
    "LPOVERLAPPED",
    "LPSECURITY_ATTRIBUTES",
    "ft_program_data",
    "PFT_PROGRAM_DATA",
    "ft_eeprom_header",
    "ft_eeprom_x_series",
    "LPFTCOMSTAT",
    "LPFTDCB",
    "FTTIMEOUTS",
    "FT_DEVICE_LIST_INFO_NODE",
    "BOOL",
    "BYTE",
    "UCHAR",
    "USHORT",
    "WORD",
    "DWORD",
    "INT",
    "ULONG",
    "ULONGLONG",
    "STRING",
    "HANDLE",
    "PVOID",
    "PCHAR",
    "PUCHAR",
    "PULONG",
    "LPVOID",
    "LPCSTR",
    "LPTSTR",
    "LPWORD",
    "LPDWORD",
    "LPLONG",
]
