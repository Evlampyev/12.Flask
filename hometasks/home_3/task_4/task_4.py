from flask import Flask, render_template, request, redirect, flash
from hometasks.home_3.task_4.model_4 import db, Users
from flask_wtf import CSRFProtect
from hometasks.home_3.task_4.form_4 import RegistrationForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///home_3_task_4_db.db'
app.config[
    'SECRET_KEY'] = '13e9aaf23f1ebb4f8f4092797a8e82567dc656cbf0f731e25baa27f072db1184'

db.init_app(app)

csrf = CSRFProtect(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        username = str(form.username.data)
        print(f'{username= }')
        password = str(form.password.data)
        print(f'{password= }')
        email = str(form.email.data)
        print(f'{email= }')
        user = Users(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        print("User added")
        flash('Вы зарегистрированы', 'success')
        return redirect('/')

    return render_template('registration.html', form=form)


@app.cli.command('db-init')
def db_init():
    db.create_all()
    print('db - OK')
