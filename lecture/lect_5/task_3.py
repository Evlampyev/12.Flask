"""Конечные точки API"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    """
    Этот код создает конечную точку для URL-адреса /items/{item_id}, которая
принимает параметр item_id типа int и параметр q типа str со значением по
умолчанию None. Если параметр q задан, функция возвращает JSON-объект с
обоими параметрами, иначе — только с item_id.
    """
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.get("/users/{user_id}/orders/{order_id}")
async def read_item(user_id: int, order_id: int):
    """
    Мы также можем определить несколько параметров URL-адреса в пути
    """
    # обработка данных
    return {"user_id": user_id, "order_id": order_id}


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
