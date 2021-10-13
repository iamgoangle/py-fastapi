### Run

```sh
$ pipenv shell
$ uvicorn main:app --reload
```

### Output

1. [http://127.0.0.1:8000](http://127.0.0.1:8000/)
2. http://127.0.0.1:8000/docs
3. http://127.0.0.1:8000/redoc

### Components

#### Starlette

Lightweight [ASGI](https://asgi.readthedocs.io/en/latest/) framework/toolkit, which is ideal for building high performance asyncio services.

#### Pydantic

Provides the Python capability data validation and setting management using annotations. Hint at runtime.

#### Uvicorn

Lightning-fast ASGI server implementation. Python has lacked a minimal low-level server/application interface for sync i/o framework. ASGI help python eco-system server to achieving high throughput in I/O Bounded context.