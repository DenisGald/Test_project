import importlib
import sys
from pathlib import Path

import pytest
from aiohttp import web

from client_generator import write_generated_client
from main import create_app


@pytest.mark.asyncio
async def test_generated_client_calls_server(
    aiohttp_client,
    workspace_tmp_path: 
        Path
):

    openapi_path = Path(__file__).resolve().parents[1] / "openapi.json"
    write_generated_client(
        openapi_path=openapi_path,
        output_dir=workspace_tmp_path
    )

    sys.path.insert(0, str(workspace_tmp_path))
    try:
        generated_client = importlib.import_module("generated_client")
        ApiClient = generated_client.ApiClient
    finally:
        sys.path.remove(str(workspace_tmp_path))
    app: web.Application = create_app()
    test_client = await aiohttp_client(app)
    base_url = str(test_client.make_url("/")).rstrip("/")

    client = ApiClient(base_url=base_url)
    msg = await client.get_hello()
    assert msg == "Работает!"

