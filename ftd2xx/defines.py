from enum import unique, IntFlag, IntEnum
import sys

# Statuses
OK = 0
INVALID_HANDLE = 1
DEVICE_NOT_FOUND = 2
DEVICE_NOT_OPENED = 3
IO_ERROR = 4
INSUFFICIENT_RESOURCES = 5
INVALID_PARAMETER = 6
INVALID_BAUD_RATE = 7
DEVICE_NOT_OPENED_FOR_ERASE = 8
DEVICE_NOT_OPENED_FOR_WRITE = 9
FAILED_TO_WRITE_DEVICE = 10
EEPROM_READ_FAILED = 11
EEPROM_WRITE_FAILED = 12
EEPROM_ERASE_FAILED = 13
EEPROM_NOT_PRESENT = 14
EEPROM_NOT_PROGRAMMED = 15
INVALID_ARGS = 16
NOT_SUPPORTED = 17
OTHER_ERROR = 18

# List Devices flags
LIST_NUMBER_ONLY = 0x80000000
LIST_BY_INDEX = 0x40000000
LIST_ALL = 0x20000000


@unique
class OpenExFlags(IntFlag):
    """Used to indicate the type of identifier being passed to FT_OpenEx."""

    OPEN_BY_SERIAL_NUMBER = 1
    OPEN_BY_DESCRIPTION = 2

    if sys.platform == "win32":
        OPEN_BY_LOCATION = 4


OPEN_BY_SERIAL_NUMBER = OpenExFlags.OPEN_BY_SERIAL_NUMBER
OPEN_BY_DESCRIPTION = OpenExFlags.OPEN_BY_DESCRIPTION
if sys.platform == "win32":
    OPEN_BY_LOCATION = OpenExFlags.OPEN_BY_LOCATION


@unique
class ModemStatus(IntFlag):
    #: Clear to Send
    CTS = 0x10

    #: Data Set Ready
    DSR = 0x20

    #: Ring Indicator
    RI = 0x40

    #: Data Carrier Detect
    DCD = 0x80

    #: Data Ready
    DR = 0x100

    #: Overrun Error
    OE = 0x200

    #: Parity Error
    PE = 0x400

    #: Framing Error
    FE = 0x800

    #: Break Interrupt
    BI = 0x1000

    #: Transmitter Holding Register
    THRE = 0x2000

    #: Transmitter Empty
    TEMT = 0x4000

    #: Receiver FIFO Error
    RCVE = 0x8000


@unique
class Device(IntEnum):
    FT_232BM = 0
    FT_232AM = 1
    FT_100AX = 2
    UNKNOWN = 3
    FT_2232C = 4
    FT_232R = 5
    FT_2232H = 6
    FT_4232H = 7
    FT_232H = 8
    FT_X_SERIES = 9


# Device Identifiers
DEVICE_232BM = Device.FT_232BM
DEVICE_232AM = Device.FT_232AM
DEVICE_100AX = Device.FT_100AX
DEVICE_UNKNOWN = Device.UNKNOWN
DEVICE_2232C = Device.FT_2232C
DEVICE_232R = Device.FT_232R
DEVICE_2232H = Device.FT_2232H
DEVICE_4232H = Device.FT_4232H
DEVICE_232H = Device.FT_232H
DEVICE_X_SERIES = Device.FT_X_SERIES


@unique
class Status(IntEnum):
    OK = 0
    INVALID_HANDLE = 1
    DEVICE_NOT_FOUND = 2
    DEVICE_NOT_OPENED = 3
    IO_ERROR = 4
    INSUFFICIENT_RESOURCES = 5
    INVALID_PARAMETER = 6
    INVALID_BAUD_RATE = 7
    DEVICE_NOT_OPENED_FOR_ERASE = 8
    DEVICE_NOT_OPENED_FOR_WRITE = 9
    FAILED_TO_WRITE_DEVICE = 10
    EEPROM_READ_FAILED = 11
    EEPROM_WRITE_FAILED = 12
    EEPROM_ERASE_FAILED = 13
    EEPROM_NOT_PRESENT = 14
    EEPROM_NOT_PROGRAMMED = 15
    INVALID_ARGS = 16
    NOT_SUPPORTED = 17
    OTHER_ERROR = 18


# Driver Types
DRIVER_TYPE_D2XX = 0
DRIVER_TYPE_VCP = 1

# Word Lengths
BITS_8 = 8
BITS_7 = 7

# Stop Bits
STOP_BITS_1 = 0
STOP_BITS_2 = 2

# Parity
PARITY_NONE = 0
PARITY_ODD = 1
PARITY_EVEN = 2
PARITY_MARK = 3
PARITY_SPACE = 4

# Flow Control
FLOW_NONE = 0x0000
FLOW_RTS_CTS = 0x0100
FLOW_DTR_DSR = 0x0200
FLOW_XON_XOFF = 0x0400

# Purge RX and TX Buffers
PURGE_RX = 1
PURGE_TX = 2

# Notification Events
EVENT_RXCHAR = 1
EVENT_MODEM_STATUS = 2
EVENT_LINE_STATUS = 4

MAX_DESCRIPTION_SIZE = 256
