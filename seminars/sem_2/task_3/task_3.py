# Создать страницу, на которой будет форма для ввода логина и пароля При нажатии на кнопку "Отправить" будет
# произведена проверка соответствия логина и пароля и переход на страницу приветствия пользователя или страницу с
# ошибкой.

from flask import Flask, url_for, render_template, request, redirect, abort

app = Flask(__name__)


@app.route('/')
def index(user: str = None):
    return render_template('index.html', context=user)


@app.get('/login/')
def login_get():
    return render_template('login.html')


@app.post('/login/')  # в маршруте мы не передаем username и password
def login_post(username: str, password: str):
    login = request.form.get('username')  # вытаскиваем их из формы
    password = request.form.get('password')
    print(login, password)
    user_data = {
        '123': ('bad@mail.ru', 'qwerty')
    }
    if (login, password) in user_data:
        return render_template(url_for('index', context=username))

    return render_template(url_for('index', context=None))


if __name__ == '__main__':
    app.run(debug=True)
