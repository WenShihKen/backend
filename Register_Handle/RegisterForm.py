from wtforms import Form, BooleanField, TextField, PasswordField, validators, StringField
from wtforms.validators import Email, InputRequired, Length, EqualTo

class RegistrationForm(Form):
    username = TextField('Username', [Length(min=5, max=15), InputRequired()])
    password = PasswordField('New Password', [
        InputRequired(),
        Length(min=5,max=15),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')