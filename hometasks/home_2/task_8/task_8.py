# Создать страницу, на которой будет форма для ввода имени и кнопка "Отправить"
# При нажатии на кнопку будет произведено перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".

from flask import Flask, request, render_template, flash, redirect

app = Flask(__name__)
app.secret_key = 'a4cf4bb73b3ef32a7f8454d20c430f74bc79789692e66faafc2dd118b7e269d6'


@app.route('/')
def index():
    return render_template('index.html')


@app.post('/flash')
def flash():
    name = request.form['user_name']
    flash(f'Привет, {name}', 'danger')
    return redirect('index.html')


if __name__ == '__main__':
    app.run(debug=True)
