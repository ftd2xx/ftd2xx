# This file was originally generated by PyScripter's unitest wizard

from builtins import str, int
import asyncio
import unittest
from .. import ftd2xx, aio
from ..ftd2xx import _ft


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
        self.assertTrue(isinstance(self.device.read(1), bytes))

    def testwrite(self):
        self.assertTrue(isinstance(self.device.write(b"%c" % 0x0), int))

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
        self.assertTrue(isinstance(self.device.getQueueStatus(), int))

    def testsetEventNotification(self):
        pass

    def testgetStatus(self):
        self.assertTrue(isinstance(self.device.getStatus(), tuple))

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
        self.assertTrue(isinstance(self.device.getLatencyTimer(), int))

    def testsetBitMode(self):
        pass

    def testgetBitMode(self):
        self.assertTrue(isinstance(self.device.getBitMode(), int))

    def testsetUSBParameters(self):
        pass

    def testgetDeviceInfo(self):
        self.assertTrue(isinstance(self.device.getDeviceInfo(), dict))

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
        self.assertTrue(isinstance(self.device.getDriverVersion(), int))

    def testeeProgram(self):
        pass

    def testeeRead(self):
        self.assertTrue(isinstance(self.device.eeRead(), ftd2xx._ft.ft_program_data))

    def testeeUASize(self):
        self.assertTrue(isinstance(self.device.eeUASize(), int))

    def testeeUAWrite(self):
        pass

    def testeeUARead(self):
        self.assertTrue(isinstance(self.device.eeUARead(5), bytes))


class TestGlobalFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testcall_ft(self):
        pass

    def testlistDevices(self):
        self.assertTrue(isinstance(ftd2xx.listDevices(), list))

    def testgetLibraryVersion(self):
        self.assertTrue(isinstance(ftd2xx.getLibraryVersion(), int))

    def testcreateDeviceInfoList(self):
        self.assertTrue(isinstance(ftd2xx.createDeviceInfoList(), int))

    def testgetDeviceInfoDetail(self):
        self.assertTrue(isinstance(ftd2xx.getDeviceInfoDetail(), dict))

    def testopen(self):
        try:
            device = ftd2xx.open()
            self.assertTrue(isinstance(device, ftd2xx.FTD2XX))
        except AssertionError:
            raise
        else:
            device.close()

    def testopenEx(self):
        try:
            dev0_id = ftd2xx.listDevices()[0]
            dev0 = ftd2xx.openEx(dev0_id)
            self.assertTrue(isinstance(dev0, ftd2xx.FTD2XX))
        except AssertionError:
            raise
        else:
            dev0.close()

    def testw32CreateFile(self):
        pass

    def testgetVIDPID(self):
        pass

    def testsetVIDPID(self):
        pass

    def testaioopen(self):
        try:
            device = aio.open()
            self.assertTrue(isinstance(device, aio.FTD2XX))
        except AssertionError:
            raise
        else:
            device.close()

    def testaioopenEx(self):
        try:
            dev0_id = aio.listDevices()[0]
            dev0 = aio.openEx(dev0_id)
            self.assertTrue(isinstance(dev0, aio.FTD2XX))
        except AssertionError:
            raise
        else:
            dev0.close()


class TestAIOFTD2XX(TestFTD2XX, unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.device = aio.open()

    async def testread(self):
        self.device.setTimeouts(1000, 0)
        result = await self.device.read(1)
        self.assertTrue(isinstance(result, bytes))


if __name__ == "__main__":
    unittest.main()
