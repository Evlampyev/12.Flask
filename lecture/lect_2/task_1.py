from markupsafe import escape
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Введи путь к файлу в адресной строке'


@app.route('/<path:file>/')
def get_file(file):
    """экранировать пользовательский ввод"""
    print(file)
    return f'Ваш файл находится в: {escape(file)}!'


if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000/<script>alert("I am haсker")</script>/
