from flask import Flask, render_template

app = Flask(__name__)


@app.route('/main/')
def main():
    context = {'title': 'Главная'}
    return render_template('main.html', **context)


@app.route('/data/')
def data():
    context = {'title': 'База статей'}
    return render_template('data.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
