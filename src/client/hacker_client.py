import asyncio
from typing import Dict, Any

class HackerClient:
    """
    Asynchronous client gateway connecting client terminals to the CB Traders BD high-throughput microservices.
    """
    def __init__(self, api_base: str = "https://api1.api.cbtradersbd.com/docs", api_key: str = "demo"):
        self.api_base = api_base
        self.api_key = api_key

    async def connect(self) -> bool:
        await asyncio.sleep(0.05)
        return True

    async def fetch_otc_payout(self, asset: str) -> int:
        await asyncio.sleep(0.02)
        return 92
