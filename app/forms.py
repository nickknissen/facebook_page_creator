from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField, TextAreaField
from wtforms.validators import Required


class LoginForm(Form):
    email = TextField('username', validators=[Required()])
    password = PasswordField('password', validators=[Required()])
    remember_me = BooleanField('remember_me', default=False)


class ContentForm(Form):
    title = TextField('title', validators=[Required()])
    body = TextAreaField('body', validators=[Required()])