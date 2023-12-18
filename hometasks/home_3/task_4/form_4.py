from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, IntegerField, EmailField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegistrationForm(FlaskForm):
    """Форма для регистрации с валидацией вводимых значений"""
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
