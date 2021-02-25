from .ftd2xx import BaseFTD2XX

class FTD2XX(BaseFTD2XX):
  async def read(self, nchars: int, raw=True):
    while not self.getQueueStatus() >= nchars:
      await asyncio.sleep(1e-3)  # Non-zero to save CPU (specific to my application, maybe there is a better general approach)
    return self._read(nchars, raw)
