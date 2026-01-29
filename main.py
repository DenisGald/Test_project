from aiohttp import web


def build_openapi_spec() -> dict:
    """
    Генерация OpenAPI-контракта (минимально, но валидно для OAS3).

    Здесь контракт генерируется кодом, чтобы он всегда соответствовал реальному API.
    """
    return {
        "openapi": "3.0.0",
        "info": {"title": "Пример Aiohttp API", "version": "v1"},
        "paths": {
            "/hello": {
                "get": {
                    "summary": "Пример эндпоинта hello",
                    "description": "Возвращает простое сообщение, чтобы проверить работу сервера.",
                    "tags": ["hello"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/HelloResponse"}
                                }
                            },
                        }
                    },
                }
            }
        },
        "components": {
            "schemas": {
                "HelloResponse": {
                    "type": "object",
                    "properties": {"message": {"type": "string"}},
                    "required": ["message"],
                    "additionalProperties": False,
                }
            }
        },
    }


async def hello(request: web.Request) -> web.Response:
    """Обработчик запроса /hello."""
    return web.json_response({"message": "Работает!"})


async def openapi_json(request: web.Request) -> web.Response:
    return web.json_response(build_openapi_spec())


def create_app() -> web.Application:
    """Фабрика приложения aiohttp."""
    app = web.Application()

    app.router.add_get("/hello", hello)
    app.router.add_get("/openapi.json", openapi_json)
    app.router.add_get("/api/docs/swagger.json", openapi_json)

    return app


def main() -> None:
    app = create_app()
    web.run_app(app, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()
