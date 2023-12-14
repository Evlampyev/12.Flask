# Создать страницу, на которой будет форма для ввода логина и пароля При нажатии на кнопку "Отправить" будет
# произведена проверка соответствия логина и пароля и переход на страницу приветствия пользователя или страницу с
# ошибкой.

from flask import Flask, url_for, render_template, request, redirect, abort

app = Flask(__name__)


@app.route('/')
@app.route('/<name>/')
def index(name: str = None):
    return render_template('index.html', username=name)


@app.get('/login/')
def login_get():
    return render_template('login.html')


@app.post('/login/')  # в маршруте мы не передаем username и password
def login_post():
    login = request.form.get('username')  # вытаскиваем их из формы
    password = request.form.get('password')
    user_data = {
        '123': ('b@ru', 'qwe')
    }
    if (login, password) == user_data.values():
        return redirect(url_for('index', name=login))
    return redirect(url_for('index', name=None))


if __name__ == '__main__':
    app.run(debug=True)
