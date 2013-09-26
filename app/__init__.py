#-*- coding: utf-8 -*-
from flask import Flask, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager


# Create Flask application
app = Flask(__name__, instance_path='/home/nkn/code/facebook_page_creator')


# Function to easily find your assets
# In your template use <link rel=stylesheet href="{{ static('filename') }}">
app.jinja_env.globals['static'] = (
    lambda filename: url_for('static', filename=filename)
)

app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)

from app import views