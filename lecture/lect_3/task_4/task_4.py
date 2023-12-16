from flask import Flask, render_template, request
from flask_wtf import CSRFProtect
from forms_4 import LoginForm, RegisterForm, RegistrationForm

app = Flask(__name__)
# Для включения защиты от CSRF-атак в Flask-WTF необходимо установить секретный
# ключ приложения
app.config['SECRET_KEY'] = '13e9aaf23f1ebb4f8f4092797a8e82567dc656cbf0f731e25baa27f072db1184'

csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Hi, from task_4'


@app.route('/data/')
def data():
    return 'Your data!'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        pass
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
