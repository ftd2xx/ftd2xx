from .mixins import *

class FTD2XX(BaseFTD2XX):
  async def read(self, length: int) -> bytes:
    while not self.getQueueStatus() >= length:
      await asyncio.sleep(1e-3)  # Non-zero to save CPU (specific to my application, maybe there is a better general approach)
    return self._read(length)
  
