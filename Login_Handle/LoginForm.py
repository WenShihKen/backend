from wtforms import Form, BooleanField, TextField, PasswordField, validators, StringField
from wtforms.validators import Email, InputRequired, Length

class LoginForm(Form):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])