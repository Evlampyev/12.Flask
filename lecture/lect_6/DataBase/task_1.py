from databases import Database
from sqlalchemy import create_engine, select, insert, update, delete, MetaData, Table, Column, Integer, String, ForeignKey
from fastapi import FastAPI
from pydantic import BaseModel, Field
from contextlib import asynccontextmanager

DATABASE_URL = "sqlite:///mydatabase.db"
# указываем в константу путь к файлу базы данных

database = Database(DATABASE_URL)

# переменная, которая будет взаимодействовать с базой данных

metadata = MetaData()

users = Table("users",
                         metadata,  # переменная, которая будет взаимодействовать с БД
                         Column("id", Integer, primary_key=True),
                         Column("name", String(32)),
                         Column("email", String(128)), )

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# создаём движок
"""
Внимание! По умолчанию SQLite разрешает взаимодействовать с ним
только одному потоку, предполагая, что каждый поток будет обрабатывать
независимый запрос. Это сделано для предотвращения случайного
использования одного и того же соединения для разных вещей (для
разных запросов). Но в FastAPI при использовании обычных функций (def)
несколько потоков могут взаимодействовать с базой данных для одного и
того же запроса, поэтому нам нужно сообщить SQLite, что он должен
разрешать это с помощью connect_args={"check_same_thread": False}.
"""

metadata.create_all(engine)
# создаём таблицы в базе данных
app = FastAPI()


class UserIn(BaseModel):
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


class User(BaseModel):
    """Сущность пользователя"""
    # Поля должны совпадать с базой данных
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


@app.on_event("startup")  # событие происходит при создании приложения
async def startup():
    await database.connect()


@app.on_event("shutdown")  # событие происходит при завершении приложения
async def shutdown():
    await database.disconnect()


# @app.get('/fake_users/{count}')
# async def create_note(count: int):
#     """
#     Создаём новые пользователей в базе данных
#     :param count: количество пользователей, которые нужно создать
#     :return: созданные пользователей в базе данных
#     """
#     for i in range(count):
#         query = users.insert().values(name=f"user{i}", email=f"mail{i}@mail.ru")
#         # создаём запрос query c полями name и email
#
#         await database.execute(query)
#         # создаём асинхронный запрос к БД для добавления туда пользователй
#
#     return {"message": f"Создано {count} пользователей"}


@app.post('/users/', response_model=User)
# response_model=User - мы обещаем вернуть модель пользователя
async def create_user(user: UserIn):
    """
    Создаём нового пользователя в базе данных
    :param user: данные нового пользователя
    :return: созданный пользователь
    """
    query = users.insert().values(name=user.name, email=user.email)
    # создаём запрос query для создания нового пользователя

    # query = users.insert().values(**user)
    # создаём запрос query для создания нового пользователя - вариант 2

    last_record_id = await database.execute(query)
    # создаём асинхронный запрос к БД для добавления нового пользователя

    return {**user.dict(), 'id': last_record_id}


@app.get('/users/')
async def users():
    """
    Получаем всех пользователей из базы данных
    :return: всех пользователей из базы данных
    """
    query = users.select()
    # создаём запрос query на получение всех пользователей

    result = await database.fetch_all(query)
    # создаём асинхронный запрос к БД для получения пользователей по запросу query
    return {'users': result}


@app.get('/users/{user_id}')
async def get_user(user_id: int):
    """Получаем пользователя по id из базы данных"""
    query = users.select().where(users.c.id == user_id)
    # создаём запрос query для выбора нужного пользователя

    result = await database.fetch_one(query)
    # создаём асинхронный запрос к БД для получения этого пользователя

    return {'user': result}


@app.put('/users/{user_id}')
async def update_user(user_id: int, user: User):
    """
    Обновляем данные пользователя по id из базы данных
    :param user_id: id пользователя
    :param user: данные пользователя
    :return: обновленные данные пользователя
    """
    query = users.update().where(users.c.id == user_id).values(name=user.name,
                                                               email=user.email)
    # создаём запрос query для обновления данными пользователя

    result = await database.execute(query)
    # создаём асинхронный запрос к БД для обновления данными пользователя

    return {'user': result}


@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    # создаём запрос query для удаления пользователя

    result = await database.execute(query)
    # создаём асинхронный запрос к БД для удаления пользователя

    return {'user': result}
