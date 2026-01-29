from __future__ import annotations

import json
from pathlib import Path


def _client_py(title: str) -> str:
    return f"""\
from dataclasses import dataclass
from typing import Any

import aiohttp


@dataclass(slots=True)
class ApiClient:
    \"\"\"Generated client for: {title}\"\"\"

    base_url: str

    async def get_hello(self) -> str:
        url = f"{{self.base_url}}/hello"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                resp.raise_for_status()
                data: Any = await resp.json()
        return str(data["message"])
"""


def write_generated_client(
    openapi_path: Path,
    output_dir: Path
):
    openapi = json.loads(openapi_path.read_text(encoding="utf-8"))

    hello_get = (((openapi.get("paths") or {}).get("/hello") or {}).get("get")) or None
    if hello_get is None:
        raise ValueError(
            "OpenAPI спецификация не содержит GET /hello"
        )

    title = str((openapi.get("info") or {}).get("title") or "OpenAPI Client")
    (output_dir / "generated_client.py").write_text(_client_py(title), encoding="utf-8")
