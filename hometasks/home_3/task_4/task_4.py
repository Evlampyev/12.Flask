from flask import Flask, render_template, request
from hometasks.home_3.task_4.model_4 import db, Users
from flask_wtf import CSRFProtect
from hometasks.home_3.task_4.form_4 import RegistrationForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///home_3_task_4_db.db'

db.init_app(app)

csrf = CSRFProtect(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registration/')
def registration():
    form = RegistrationForm()
    return render_template('registration.index', form=form)

    @app.cli.command('db-init')
    def db_init():
        db.create_all()
        print('db - OK')
