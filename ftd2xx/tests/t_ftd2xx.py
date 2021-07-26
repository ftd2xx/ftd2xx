# This file was originally generated by PyScripter's unitest wizard

import unittest
from builtins import int, str

from .. import ftd2xx
from ..ftd2xx import DeviceError


class TestDeviceError(unittest.TestCase):
    def setUp(self):
        self.expt = ftd2xx.DeviceError(0)

    def tearDown(self):
        pass

    def test__str__(self):
        self.assertTrue(str(self.expt) == "OK")


class TestFTD2XX(unittest.TestCase):
    def setUp(self):
        self.device = ftd2xx.open()

    def tearDown(self):
        self.device.close()

    def testclose(self):
        pass

    def testread(self):
        self.device.setTimeouts(1000, 0)
        self.assertIsInstance(self.device.read(1), bytes)

    def testwrite(self):
        self.assertIsInstance(self.device.write(b"\x00"), int)

    def testioctl(self):
        pass

    def testsetBaudRate(self):
        pass

    def testsetDivisor(self):
        pass

    def testsetDataCharacteristics(self):
        pass

    def testsetFlowControl(self):
        pass

    def testresetDevice(self):
        pass

    def testsetDtr(self):
        pass

    def testclrDtr(self):
        pass

    def testsetRts(self):
        pass

    def testclrRts(self):
        pass

    def testgetModemStatus(self):
        pass

    def testsetChars(self):
        pass

    def testpurge(self):
        pass

    def testsetTimeouts(self):
        pass

    def testsetDeadmanTimeout(self):
        pass

    def testgetQueueStatus(self):
        self.assertIsInstance(self.device.getQueueStatus(), int)

    def testsetEventNotification(self):
        pass

    def testgetStatus(self):
        self.assertIsInstance(self.device.getStatus(), tuple)

    def testsetBreakOn(self):
        pass

    def testsetBreakOff(self):
        pass

    def testsetWaitMask(self):
        pass

    def testwaitOnMask(self):
        pass

    def testgetEventStatus(self):
        pass

    def testsetLatencyTimer(self):
        pass

    def testgetLatencyTimer(self):
        self.assertIsInstance(self.device.getLatencyTimer(), int)

    def testsetBitMode(self):
        pass

    def testgetBitMode(self):
        self.assertIsInstance(self.device.getBitMode(), int)

    def testsetUSBParameters(self):
        pass

    def testgetDeviceInfo(self):
        self.assertIsInstance(self.device.getDeviceInfo(), dict)

    def teststopInTask(self):
        pass

    def testrestartInTask(self):
        pass

    def testsetRestPipeRetryCount(self):
        pass

    def testresetPort(self):
        pass

    def testcyclePort(self):
        pass

    def testgetDriverVersion(self):
        self.assertIsInstance(self.device.getDriverVersion(), int)

    def testeeProgram(self):
        pass

    def testeeRead(self):
        self.assertIsInstance(self.device.eeRead(), ftd2xx._ft.ft_program_data)

    def testeeUASize(self):
        self.assertIsInstance(self.device.eeUASize(), int)

    def testeeUAWrite(self):
        pass

    def testeeUARead(self):
        self.assertIsInstance(self.device.eeUARead(5), bytes)


class TestGlobalFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testcall_ft(self):
        pass

    def testlistDevices(self):
        self.assertIsInstance(ftd2xx.listDevices(), list)

    def testgetLibraryVersion(self):
        self.assertIsInstance(ftd2xx.getLibraryVersion(), int)

    def testcreateDeviceInfoList(self):
        self.assertIsInstance(ftd2xx.createDeviceInfoList(), int)

    def testgetDeviceInfoDetail(self):
        self.assertIsInstance(ftd2xx.getDeviceInfoDetail(), dict)

    def testopen(self):
        try:
            device = ftd2xx.open()
            self.assertIsInstance(device, ftd2xx.FTD2XX)
        except AssertionError:
            raise
        else:
            device.close()

    def testopenEx(self):
        dev0 = None
        try:
            devices = ftd2xx.listDevices()
            if devices is None:
                raise DeviceError("Device not found")
            dev0_id = devices[0]
            dev0 = ftd2xx.openEx(dev0_id)
            self.assertIsInstance(dev0, ftd2xx.FTD2XX)
            self.assertEqual(dev0.getDeviceInfo()["serial"], dev0_id)
        except AssertionError:
            raise
        finally:
            if dev0:
                dev0.close()
