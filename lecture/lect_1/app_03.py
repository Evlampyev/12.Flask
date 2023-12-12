"""Прописываем логику обработки URL"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<name>/')
def hello(name='незнакомец'):
    """Функция представление"""
    return f'Привет, {name.capitalize()}!'


@app.route('/file/<path:file>/')  # В треугольных скобках (file) - переменная
def set_path(file):
    print(type(file))
    return f'Путь до файла "{file}"'


@app.route('/number/<float:num>/')
# переменная num, работе только положительные числа с точкой
def set_number(num):
    print(type(num))
    return f'Передано число {num}'


if __name__ == '__main__':
    app.run(debug=True)
