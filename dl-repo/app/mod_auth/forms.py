# Import Form and RecaptchaField (optional)
from flask.ext.wtf import Form # , RecaptchaField

from wtforms import TextField, PasswordField # BooleanField
from wtforms.validators import Required, Email, EqualTo

# Define the login form
class LoginForm(Form):
    email = TextField('Email Address', [Email(),
        Required(message='Forgot your email address?')])
    password = PasswordField('Password', [
        Required(message='Must provide a password. ;-)')])
