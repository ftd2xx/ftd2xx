"""FTD2XX EEPROM Programming Interface"""
from .typedefs import (
    FT_HANDLE,
    FT_STATUS,
    PFT_PROGRAM_DATA,
    WORD,
    DWORD,
    STRING,
    PVOID,
    PUCHAR,
    LPWORD,
    LPDWORD,
)

# pylint: disable=C0103
# pylint: disable=unused-argument
# pylint: disable=too-many-arguments


def FT_ReadEE(ftHandle: FT_HANDLE, dwWordOffset: DWORD, lpwValue: LPWORD) -> FT_STATUS:
    """Read a value from an EEPROM location.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        dwWordOffset (DWORD): EEPROM location to read from.
        lpwValue (LPWORD): Pointer to the WORD value read from the EEPROM.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_WriteEE(ftHandle: FT_HANDLE, dwWordOffset: DWORD, wValue: WORD) -> FT_STATUS:
    """Write a value to an EEPROM location.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        dwWordOffset (DWORD): EEPROM location to write to.
        wValue (WORD): The WORD value write to the EEPROM.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_EraseEE(ftHandle: FT_HANDLE) -> FT_STATUS:
    """Erases the device EEPROM.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_EE_Read(ftHandle: FT_HANDLE, pData: PFT_PROGRAM_DATA) -> FT_STATUS:
    """Read the contents of the EEPROM.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        pData (PFT_PROGRAM_DATA): Pointer to structure of type FT_PROGRAM_DATA.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_EE_ReadEx(
    ftHandle: FT_HANDLE,
    pData: PFT_PROGRAM_DATA,
    Manufacturer: STRING,
    ManufacturerId: STRING,
    Description: STRING,
    SerialNumber: STRING,
) -> FT_STATUS:
    """Read the contents of the EEPROM and pass strings separately.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        pData (PFT_PROGRAM_DATA): Pointer to structure of type FT_PROGRAM_DATA.
        Manufacturer (STRING): Pointer to a null-terminated string containing the manufacturer
            name.
        ManufacturerId (STRING): Pointer to a null-terminated string containing the manufacturer
            ID.
        Description (STRING): Pointer to a null-terminated string containing the device
            description.
        SerialNumber (STRING): Pointer to a null-terminated string containing the device serial
            number.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_EE_Program(ftHandle: FT_HANDLE, pData: PFT_PROGRAM_DATA) -> FT_STATUS:
    """Program the EEPROM.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        pData (PFT_PROGRAM_DATA): Pointer to structure of type FT_PROGRAM_DATA.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_EE_ProgramEx(
    ftHandle: FT_HANDLE,
    pData: PFT_PROGRAM_DATA,
    Manufacturer: STRING,
    ManufacturerId: STRING,
    Description: STRING,
    SerialNumber: STRING,
) -> FT_STATUS:
    """Program the EEPROM and pass strings separately.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        pData (PFT_PROGRAM_DATA): Pointer to structure of type FT_PROGRAM_DATA.
        Manufacturer (STRING): Pointer to a null-terminated string containing the manufacturer
            name.
        ManufacturerId (STRING): Pointer to a null-terminated string containing the manufacturer
            ID.
        Description (STRING): Pointer to a null-terminated string containing the device
            description.
        SerialNumber (STRING): Pointer to a null-terminated string containing the device serial
            number.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_EE_UASize(ftHandle: FT_HANDLE, lpdwSize: LPDWORD) -> FT_STATUS:
    """Get the available size of the EEPROM user area.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        lpdwSize (LPDWORD): Pointer to a DWORD that receives the available size, in bytes, of the
            EEPROM user area.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_EE_UARead(
    ftHandle: FT_HANDLE,
    pucData: PUCHAR,
    dwDataLen: DWORD,
    lpdwBytesRead: LPDWORD,
) -> FT_STATUS:
    """Read the contents of the EEPROM user area.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        pucData (PUCHAR): Pointer to a buffer that contains storage for data to be read.
        dwDataLen (DWORD): Size, in bytes, of buffer that contains storage for the data to be read.
        lpdwBytesRead (LPDWORD): Pointer to a DWORD that receives the number of bytes read.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_EE_UAWrite(ftHandle: FT_HANDLE, pucData: PUCHAR, dwDataLen: DWORD) -> FT_STATUS:
    """Write data into the EEPROM user area.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        pucData (PUCHAR): Pointer to a buffer that contains storage for data to be written.
        dwDataLen (DWORD): Size, in bytes, of buffer that contains storage for the data to be
            written.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_EEPROM_Read(
    ftHandle: FT_HANDLE,
    eepromData: PVOID,
    eepromDataSize: DWORD,
    Manufacturer: STRING,
    ManufacturerId: STRING,
    Description: STRING,
    SerialNumber: STRING,
) -> FT_STATUS:
    """Read data from the EEPROM, this command will work for all existing FTDI chipset, and must be
    used for the FT-X series.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        pData (PVOID): Pointer to a buffer that contains the data to be read.
        eepromDataSize (DWORD): Size of the eepromData buffer that contains storage for the data to
            be read.
        Manufacturer (STRING): Pointer to a null-terminated string containing the manufacturer
            name.
        ManufacturerId (STRING): Pointer to a null-terminated string containing the manufacturer
            ID.
        Description (STRING): Pointer to a null-terminated string containing the device
            description.
        SerialNumber (STRING): Pointer to a null-terminated string containing the device serial
            number.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


def FT_EEPROM_Program(
    ftHandle: FT_HANDLE,
    eepromData: PVOID,
    eepromDataSize: DWORD,
    Manufacturer: STRING,
    ManufacturerId: STRING,
    Description: STRING,
    SerialNumber: STRING,
) -> FT_STATUS:
    """Write data into the EEPROM, this command will work for all existing FTDI chipset, and must
    be used for the FT-X series.

    Args:
        ftHandle (FT_HANDLE): Handle of the device.
        pData (PVOID): Pointer to a buffer that contains the data to be written.
        eepromDataSize (DWORD): Size of the eepromData buffer that contains storage for the data to
            be written.
        Manufacturer (STRING): Pointer to a null-terminated string containing the manufacturer
            name.
        ManufacturerId (STRING): Pointer to a null-terminated string containing the manufacturer
            ID.
        Description (STRING): Pointer to a null-terminated string containing the device
            description.
        SerialNumber (STRING): Pointer to a null-terminated string containing the device serial
            number.

    Returns:
        FT_OK if successful, otherwise the return value is an FT error code.
    """


__all__ = [
    "FT_ReadEE",
    "FT_WriteEE",
    "FT_EraseEE",
    "FT_EE_Read",
    "FT_EE_ReadEx",
    "FT_EE_Program",
    "FT_EE_ProgramEx",
    "FT_EE_UASize",
    "FT_EE_UARead",
    "FT_EE_UAWrite",
    "FT_EEPROM_Read",
    "FT_EEPROM_Program",
]
