import pytest
from aiohttp import web

from main import create_app


@pytest.mark.asyncio
async def test_hello_endpoint(aiohttp_client):
    app: web.Application = create_app()
    client = await aiohttp_client(app)

    resp = await client.get("/hello")
    assert resp.status == 200

    data = await resp.json()
    assert data["message"] == "Работает!"


@pytest.mark.asyncio
async def test_openapi_spec_available(aiohttp_client):
    app: web.Application = create_app()
    client = await aiohttp_client(app)

    resp = await client.get("/api/docs/swagger.json")
    assert resp.status == 200

    data = await resp.json()
    assert isinstance(data, dict)
    assert data.get("info", {}).get("title") == "Пример Aiohttp API"
    assert "/hello" in (data.get("paths") or {})
    assert "get" in ((data.get("paths") or {}).get("/hello") or {})

