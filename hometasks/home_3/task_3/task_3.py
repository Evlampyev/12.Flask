from hometasks.home_3.task_3.model_3 import db, Students, Scores, Items
from flask import render_template, request, redirect, url_for, flash, Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///home_3_task_3_db.db'

db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')
