from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/about/')
def about():
    return render_template('about_2.html')


@app.route('/contacts/')
def contacts():
    return render_template('contacts_2.html')


if __name__ == '__main__':
    app.run(debug=True)
