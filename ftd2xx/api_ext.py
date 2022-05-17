"""FTD2XX Extended API"""
from .typedefs import (
    FT_HANDLE,
    FT_STATUS,
    UCHAR,
    ULONG,
    PUCHAR,
)

# pylint: disable=C0103
# pylint: disable=unused-argument
# pylint: disable=too-many-arguments


def FT_SetLatencyTimer(ftHandle: FT_HANDLE, ucLatency: UCHAR) -> FT_STATUS:
    """Set the latency timer value.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        ucLatency (UCHAR): Required value, in milliseconds, of latency timer. Valid range is 2 -
            255.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_GetLatencyTimer(ftHandle: FT_HANDLE, pucLatency: PUCHAR) -> FT_STATUS:
    """Get the current value of the latency timer.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        pucLatency (PUCHAR): Pointer to unsigned char to store latency timer value.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_SetBitMode(ftHandle: FT_HANDLE, ucMask: UCHAR, ucEnable: UCHAR) -> FT_STATUS:
    """Enables different chip modes.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        ucMask (UCHAR): Required value for bit mode mask. This sets up which bits are inputs and
            outputs. A bit value of 0 sets the corresponding pin to an input, a bit value of 1 sets
            the corresponding pin to an output.

            In the case of CBUS Bit Bang, the upper nibble of this value controls which pins are
            inputs and outputs,	while the lower nibble controls which of the outputs are high and
            low.
        ucEnable (UCHAR): Mode value. Can be one of the following:
            * 0x0 = Reset
            * 0x1 = Asynchronous Bit Bang
            * 0x2 = MPSSE (FT2232, FT2232H, FT4232H and FT232H devices only)
            * 0x4 = Synchronous Bit Bang (FT232R, FT245R, FT2232, FT2232H, FT4232H and FT232H
                devices only)
            * 0x8 = MCU Host Bus Emulation Mode (FT2232, FT2232H, FT4232H and FT232H devices only)
            * 0x10 = Fast Opto-Isolated Serial Mode (FT2232, FT2232H, FT4232H and FT232H devices
                only)
            * 0x20 = CBUS Bit Bang Mode (FT232R and FT232H devices only)
            * 0x40 = Single Channel Synchronous 245 FIFO Mode (FT2232H and FT232H devices only)

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_GetBitMode(ftHandle: FT_HANDLE, pucMode: PUCHAR) -> FT_STATUS:
    """Gets the instantaneous value of the data bus.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        pucMode (PUCHAR): Pointer to unsigned char to store the instantaneous data bus value.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_SetUSBParameters(
    ftHandle: FT_HANDLE,
    ulInTransferSize: ULONG,
    ulOutTransferSize: ULONG,
) -> FT_STATUS:
    """Set the USB request transfer size.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        ulInTransferSize (ULONG): Transfer size for USB IN request.
        ulOutTransferSize (ULONG): Transfer size for USB OUT request.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


__all__ = [
    "FT_SetLatencyTimer",
    "FT_GetLatencyTimer",
    "FT_SetBitMode",
    "FT_GetBitMode",
    "FT_SetUSBParameters",
]
