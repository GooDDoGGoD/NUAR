from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Еmail', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    surname = StringField('Ник', validators=[DataRequired()])
    # name = StringField('Имя', validators=[DataRequired()])
    # age = StringField('Возраст', validators=[DataRequired()])
    # position = StringField('Позиция', validators=[DataRequired()])
    # speciality = StringField('Специальность', validators=[DataRequired()])
    # address = StringField('Адрес', validators=[DataRequired()])
    submit = SubmitField('Продолжить')
