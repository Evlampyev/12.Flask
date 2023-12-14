# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.

from flask import Flask, render_template, request, url_for, redirect, abort

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


@app.post('/verification/')
def verification():
    user_name = request.form.get('user_name').title()
    user_age = request.form.get('age')
    print(f'{user_name = } {user_age = }')
    if int(user_age) >= 18:
        return render_template('good_age.html', name=user_name, age=user_age)
    else:
        return render_template('bad_age.html', age=(18-int(user_age)))


if __name__ == '__main__':
    app.run(debug=True)
