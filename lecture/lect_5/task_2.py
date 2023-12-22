from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
import logging

# pydantic поддерживает валидацию, проверку на тип


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


# Optional - это опциональный параметр, который может быть указан по умолчанию


@app.get('/')
async def read_root():
    """Метод GET для получения ресурсов с сервера"""
    logger.info('Отработал GET запрос')
    return {"message": 'Hello World'}


"""
@app.get('/items/{item_id}/')
async def read_item(item_id: int, q: str = None):
    #  /items/34/?q=%27werwre%27 - по такому пути
    #  будет выдано {"item_id":34,"q":"'werwre'"}
    return {'item_id': item_id, 'q': q}
"""


@app.post('/items/')
async def create_item(item: Item):
    """"Метод POST для отправки новых данных на сервер"""
    logger.info('Отработал POST запрос')
    return item


@app.put('/items/{item_id}/')
async def update_item(item_id: int, item: Item):
    """Обновление (изменение существующих) данных на сервере"""
    logger.info(f'Отработал PUT запрос для item_id={item_id}.')
    return {'item_id': item_id, 'item': item}


@app.delete('/items/{item_id}/')
async def delete_item(item_id: int):
    """Удаление данных на сервере"""
    # Рекомендуется не удалять, а менять свойство is_active=False
    logger.info(f'Отработал DELETE запрос для item_id={item_id}.')
    return {'item_id': item_id}
