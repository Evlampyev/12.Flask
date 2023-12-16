from flask import Flask
from flask_wtf import FlaskForm, CSRFProtect

app = Flask(__name__)
# Для включения защиты от CSRF-атак в Flask-WTF необходимо установить секретный
# ключ приложения
app.config['SECRET_KEY'] = '13e9aaf23f1ebb4f8f4092797a8e82567dc656cbf0f731e25baa27f072db1184'

csrf = CSRFProtect(app)


# Создаем объект csrf и передаем ему приложение Flask. Затем мы
# устанавливаем секретный ключ приложения. После этого защита от CSRF-атак
# будет включена для всех форм в приложении


@app.route('/form', methods=['GET', 'POST'])
@csrf.exempt  # отключить защиту от CSRF-атак для определенной формы, вы можете использовать декоратор csrf.exempt
def my_form():
    return "Эта форма без защиты"
