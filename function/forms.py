from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, IntegerField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, NumberRange, Email

class loginForm(FlaskForm):
    user_id = StringField('user_id', validators=[DataRequired('Required')])
    password = PasswordField('password', validators=[DataRequired('Required')])