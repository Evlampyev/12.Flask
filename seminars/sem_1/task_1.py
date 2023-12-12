from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return 'Hello, World!'


@app.route('/about/')
def about():
    return 'Info about me'


@app.route('/contact')
def contact():
    return 'My tel: 8-922'


@app.route('/<int:num1>/<int:num2>/')
def summa(num1: int, num2: int):
    """Сумма двух чисел"""
    return f'{num1} + {num2} = {num1 + num2}'


@app.route('/string/<string:data>/')
def len_str(data: str):
    """Длина строки"""
    return f'Длина строки {data} = {len(data)}'


@app.route('/index/')
def index():
    """Вывод на экран HTML страницу"""
    html = """
    <title>Моя первая страница</title>
    <p>Привет, Мир!</p>
    """
    return html


@app.route('/students/')
def students():
    context = [{
            'name'         : 'Александр',
            'second_name'     : 'Иванов',
            'age'     : 25,
            'average_score': 4.7
        }, {
            'name'         : 'Надежда',
            'second_name'     : 'Иванова',
            'age'     : 23,
            'average_score': 4.8
        }]

    return render_template('index.html', students=context)


if __name__ == '__main__':
    app.run(debug=True)
