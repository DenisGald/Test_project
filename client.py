from dataclasses import dataclass

import aiohttp


@dataclass(slots=True)
class HelloApiClient:
    base_url: str

    async def get_hello(self) -> str:
        url = f"{self.base_url}/hello"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                resp.raise_for_status()
                data = await resp.json()

        return str(data["message"])

