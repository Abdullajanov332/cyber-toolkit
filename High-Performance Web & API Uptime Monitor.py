"""
Cyber Security Toolkit - High-Performance Web Monitor
Author: @abdullajaanov
Role: Chief Cyber Architect
"""

import asyncio
import http
import logging
from typing import List, Dict
import urllib.request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("WebMonitor")

class HighPerformanceWebMonitor:
    """Asynchronous concurrent network-service availability monitor."""
    
    def __init__(self, targets: List[str]) -> None:
        self.targets = targets

    async def _probe_target(self, url: str) -> Dict[str, Any]:
        """Non-blocking low-level connection pool tester."""
        # Running synchronous IO in executor thread pool to maximize async throughput
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, self._sync_probe, url)

    def _sync_probe(self, url: str) -> Dict[str, Any]:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'CyberArchitect-Monitor/@abdullajaanov'})
            with urllib.request.urlopen(req, timeout=5) as response:
                status = response.getcode()
                return {"url": url, "status": status, "alive": status == http.HTTPStatus.OK}
        except Exception as e:
            return {"url": url, "status": None, "alive": False, "error": str(e)}

    async def execution_loop(self) -> None:
        logger.info("[*] Starting Core Concurrency Matrix by @abdullajaanov")
        tasks = [self._probe_target(url) for url in self.targets]
        results = await asyncio.gather(*tasks)
        
        for result in results:
            if result["alive"]:
                logger.info(f"[ONLINE] {result['url']} returned Status: {result['status']}")
            else:
                logger.critical(f"[OFFLINE/MALFUNCTION] Alert on {result['url']}. Error Context: {result.get('error')}")

if __name__ == "__main__":
    mon = HighPerformanceWebMonitor(["https://www.google.com", "https://api.github.com"])
    asyncio.run(mon.execution_loop())
