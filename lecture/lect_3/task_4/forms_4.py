from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo


# WTForms позволяет проводить валидацию данных формы

class LoginForm(FlaskForm):
    # validators - Для того, чтобы требовать от пользователя заполнения полей
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    """Форма для заполнения после регистрации"""
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'Мужчина'), ('female', 'Женщина')])


class RegistrationForm(FlaskForm):
    """Форма для регистрации с валидацией вводимых значений"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

# pip install email-validator
