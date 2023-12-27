# Создать API для добавления нового пользователя в базу данных. Приложение
# должно иметь возможность принимать POST запросы с данными нового
# пользователя и сохранять их в базу данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя (метод POST).
# Реализуйте валидацию данных запроса и ответа.

from fastapi import FastAPI
from seminars.sem_5.pack_3.models_3 import User

app = FastAPI()

users: list[User] = []


@app.get('/')
async def read_root():
    """Получение списка пользователей"""
    return users


@app.post('/users')
async def create_users(user: User):
    """Добавление нового пользователя в базу данных"""
    users.append(user)
    return user


@app.put('/users/{user_id}')
async def update_users(user_id: int, new_user: User):
    """Обновление данных пользователя"""
    filtered_users = [user for user in users if user.id == user_id]
    if not filtered_users:
        return {'message': 'User not found'}
    user = filtered_users[0]
    user.name = new_user.name
    user.email = new_user.email
    user.password = new_user.password
    return {'message': 'User updated', 'user': new_user}


@app.delete('/users/{user_id}')
async def delete_users(user_id: int):
    """Удаление данных пользователя"""
    filtered_users = [user for user in users if user.id == user_id]
    if not filtered_users:
        return {'message': 'User not found'}
    users.remove(filtered_users[0])
    return {'message': 'User deleted', 'user': filtered_users[0]}