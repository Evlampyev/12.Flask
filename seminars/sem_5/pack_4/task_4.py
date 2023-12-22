# Создать веб-страницу для отображения списка пользователей. Приложение
# должно использовать шаблонизатор Jinja для динамического формирования HTML
# страницы.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
# содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.

from fastapi import FastAPI, Request, Response, Form
from seminars.sem_5.pack_4.models_5 import User
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory='seminars/sem_5/pack_4/templates')
users: list[User] = []


@app.get('/', response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.post('/')
async def add_users(request: Request,
                    name: str = Form(...),
                    email: str = Form(...),
                    password: str = Form(...),
                    id: int = Form(...)):
    form = Form()
    if request.method == 'POST':
        user = User(name=request.form['name'], email=request.form['email'], )


@app.post('/users/')
async def create_users(user: User):
    users.append(user)
    return user


@app.put('/users/{user_id}')
async def update_users(user_id: int, new_user: User):
    filtered_users = [user for user in users if user.id == user_id]
    if not filtered_users:
        return {'message': 'User not found'}
    user = filtered_users[0]
    user.name = new_user.name
    user.email = new_user.email
    user.password = new_user.password
    return {'message': 'User updated', 'user': new_user}
