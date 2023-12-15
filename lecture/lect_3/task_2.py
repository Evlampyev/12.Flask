from flask import Flask
from lecture.lect_3.model_02 import db, User, Post, Comment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'


@app.cli.command("init-db")
def init_db():
    """Покажет ошибку с неверным wsgi.py"""
    db.create_all()
    print('OK')


if __name__ == '__main__':
    app.run(debug=True)
