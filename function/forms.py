from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, IntegerField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, NumberRange, Email

class loginForm(FlaskForm):
    user_id = StringField('user_id', validators=[DataRequired('Required')])
    password = PasswordField('password', validators=[DataRequired('Required')])

class registerForm(FlaskForm):
    user_id = StringField('user_id', validators=[DataRequired('Required'), Length(min=3, max=16)])
    user_name = StringField('user_name', validators=[DataRequired('Required'), Length(min=3, max=16)])
    user_email = EmailField('email', validators=[DataRequired('Required'), Email()])
    password = PasswordField('password', validators=[DataRequired('Required'), Length(min=8)])