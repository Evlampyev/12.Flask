from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Привет, незнакомец!'


@app.route('/Николай/')
def nike():
    return 'Привет, Николай!'


@app.route(
    '/Иван/')  # множественное декорирование для одного результата при разных адресах
@app.route('/Ваня/')
@app.route('/Vanek/')
def ivan():
    return 'Привет, Иван!'


if __name__ == '__main__':
    app.run(debug=True)
