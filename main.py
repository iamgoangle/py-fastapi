from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    resp = {
        "firstname": "Prayuth",
        "lastname": "Juneieie",
        "year": 65,
    }

    return resp


@app.get("/items/{id}")
async def get_item_handler(id: int):
    resp = {
        "id": id,
        "name": "my product"
    }

    return resp


@app.get("/products/")
async def product_handler(page: int = 1, limit:  Optional[int] = 10):

    resp = {
        "page": page,
        "limit": limit
    }

    return resp
