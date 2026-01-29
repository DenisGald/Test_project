## Проект: Тестовое задание aiohttp и OpenAPI

### Запуск

- **Установка зависимостей**

```bash
pip install -r requirements.txt
```

- **Запуск сервера**

```bash
python main.py
```

Сервер поднимается на `http://localhost:8080`.

- **Проверка эндпоинта**

```bash
curl http://localhost:8080/hello
```

- **Swagger UI и OpenAPI JSON**

- **OpenAPI JSON**: `http://localhost:8080/openapi.json` (алиас: `/api/docs/swagger.json`)

### Клиент на aiohttp

- **Файл клиента**: `client.py`
- **Пример запуска**

```bash
python client.py
```

Клиент использует `aiohttp.ClientSession` и обращается к `GET /hello`.

### Генерация клиента из OpenAPI контрактов

В этом тестовом задании клиент генерируется утилитой из `openapi.json`:

- **Генератор**: `generated_client_generator.py`
- **Контракт**: `openapi.json`


### Тесты

- **Запуск всех тестов**

```bash
python -m pytest
```
