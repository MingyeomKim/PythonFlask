from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegisterationFrom(FlaskForm):
    username = StringField("아이디",validators = [DataRequired(), Length(min=4,max=20)])
    email = StringField()