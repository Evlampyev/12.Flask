# Создать страницу, на которой будет кнопка "Нажми меня", при
# нажатии на которую будет переход на другую страницу с
# приветствием пользователя по имени.

from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def index():
    data = {
        'name': 'Данил'
    }
    return render_template('task_1/index.html', **data)


@app.route('/greet/<name>')
def greet(name: str):
    print(url_for('greet', name='Danil'))
    return render_template('task_1/name.html', context=name)


if __name__ == "__main__":
    app.run(debug=True)