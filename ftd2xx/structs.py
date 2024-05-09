import ctypes
from ctypes.wintypes import DWORD, WORD, ULONG, HANDLE, BYTE
from typing import Any
from typing_extensions import Self

UCHAR = ctypes.c_ubyte
FT_HANDLE = HANDLE
FT_STATUS = ULONG

# values for unnamed enumeration
PFT_EVENT_HANDLER = ctypes.CFUNCTYPE(None, ctypes.c_ulong, ctypes.c_ulong)
FT_DEVICE = ULONG


class ft_eeprom_header(ctypes.Structure):
    __fields__ = [
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


class ft_eeprom_232b(ctypes.Structure):
    __fields__ = [
        # Common header
        ("common", ft_eeprom_header)  # common elements for all device EEPROMs
    ]


class ft_eeprom_2232(ctypes.Structure):
    __fields__ = [
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


class ft_eeprom_232r(ctypes.Structure):
    __fields__ = [
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


class ft_eeprom_2232h(ctypes.Structure):
    __fields__ = [
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


class ft_eeprom_4232h(ctypes.Structure):
    __fields__ = [
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


class ft_eeprom_232h(ctypes.Structure):
    __fields__ = [
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


class ft_eeprom_x_series(ctypes.Structure):
    __fields__ = [
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


class StructureWithDefaults(ctypes.Structure):
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
    __fields__ = [
        ("DCBlength", DWORD),  # sizeof(FTDCB)
        ("BaudRate", DWORD),  # Baud rate at which running
        ("fBinary", DWORD),  # Binary Mode (skip EOF check)
        ("fParity", DWORD),  # Enable parity checking
        ("fOutxCtsFlow", DWORD),  # CTS handshaking on output
        ("fOutxDsrFlow", DWORD),  # DSR handshaking on output
        ("fDtrControl", DWORD),  # DTR Flow control
        ("fDsrSensitivity", DWORD),  # DSR Sensitivity
        ("fTXContinueOnXoff", DWORD),  # Continue TX when Xoff sent
        ("fOutX", DWORD),  # Enable output X-ON/X-OFF
        ("fInX", DWORD),  # Enable input X-ON/X-OFF
        ("fErrorChar", DWORD),  # Enable Err Replacement
        ("fNull", DWORD),  # Enable Null stripping
        ("fRtsControl", DWORD),  # Rts Flow control
        ("fAbortOnError", DWORD),  # Abort all reads and writes on Error
        ("fDummy2", DWORD),  # Reserved
        ("wReserved", WORD),  # Not currently used
        ("XonLim", WORD),  # Transmit X-ON threshold
        ("XoffLim", WORD),  # Transmit X-OFF threshold
        ("ByteSize", BYTE),  # Number of bits/byte, 7-8
        ("Parity", BYTE),  # 0-4=None,Odd,Even,Mark,Space
        ("StopBits", BYTE),  # 0,2 = 1, 2
        ("XonChar", ctypes.c_char),  # Tx and Rx X-ON character
        ("XoffChar", ctypes.c_char),  # Tx and Rx X-OFF character
        ("ErrorChar", ctypes.c_char),  # Error replacement char
        ("EofChar", ctypes.c_char),  # End of Input character
        ("EvtChar", ctypes.c_char),  # Received Event character
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


class FTTIMEOUTS(ctypes.Structure):
    __fields__ = [
        ("ReadIntervalTimeout", DWORD),  # Maximum time between read chars
        ("ReadTotalTimeoutMultiplier", DWORD),  # Multiplier of characters
        ("ReadTotalTimeoutConstant", DWORD),  # Constant in milliseconds
        ("WriteTotalTimeoutMultiplier", DWORD),  # Multiplier of characters
        ("WriteTotalTimeoutConstant", DWORD),  # Constant in milliseconds
    ]


class FTCOMSTAT(StructureWithDefaults):
    __fields__ = [
        ("fCtsHold", DWORD),
        ("fDsrHold", DWORD),
        ("fRlsdHold", DWORD),
        ("fXoffHold", DWORD),
        ("fXoffSent", DWORD),
        ("fEof", DWORD),
        ("fTxim", DWORD),
        ("fReserved", DWORD),
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
