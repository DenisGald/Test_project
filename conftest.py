import pytest
from aiohttp.test_utils import TestClient, TestServer
from pathlib import Path
from uuid import uuid4


@pytest.fixture
def aiohttp_client(event_loop):
    created: list[TestClient] = []

    async def _make_client(app):
        server = TestServer(app)
        await server.start_server()
        client = TestClient(server)
        await client.start_server()
        created.append(client)
        return client

    yield _make_client

    for client in created:
        event_loop.run_until_complete(client.close())


@pytest.fixture
def workspace_tmp_path() -> Path:
    root = Path(__file__).resolve().parent / "._pytest_tmp"
    root.mkdir(parents=True, exist_ok=True)
    p = root / uuid4().hex
    p.mkdir(parents=True, exist_ok=True)
    return p

