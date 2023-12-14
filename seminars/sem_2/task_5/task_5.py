from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.post('/result/')
def result():
    res = 0
    first = int(request.form.get('first'))
    second = int(request.form.get('second'))
    operation = request.form.get('operation')
    if operation in '+-/*':
        res = eval(f'{first}{operation}{second}')  # вычисляет строку
    else:
        res = 'Ошибка'
    return render_template('result.html', res=res)


if __name__ == '__main__':
    app.run(debug=True)
