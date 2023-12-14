"""Перенаправление"""

from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/external')  # При переходе на страницу /external будет перенаправление
def external_redirect():
    return redirect('https://google.com')


@app.route('/hello/<name>')
def hello(name):
    return f'Привет, {name}!'


@app.route('/redirect/<name>')
def redirect_to_hello(name):
    return redirect(url_for('hello', name=name))


if __name__ == '__main__':
    app.run(debug=True)
