from flask import render_template, flash, redirect, url_for, g, request
from flask.ext.login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, \
    check_password_hash
from app import app, lm
from app.forms import LoginForm
from app.models import User, db


@app.route('/')
@app.route('/index')
def index():
    print(g.user)
    if g.user is not None and g.user.is_authenticated():

        return redirect(url_for('pages'))
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    f = request.form
    if current_user.is_authenticated():
        return redirect(url_for('pages'))
    form = LoginForm()
    if form.validate_on_submit():
        validate_user(f['email'], f['password'], f['remember_me'])
    return render_template('login.html', title='Log ind', form=form)


@app.route('/pages')
@login_required
def pages():
    return render_template('pages.html')


def validate_user(email, password, remember_me=None):
    if email and password:
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):

                login_user(user, remember=remember_me)
                return user


def create_user(email, password):
    user = User(email, generate_password_hash(password))
    db.session.add(user)
    db.session.commit()


@app.before_request
def before_request():
    g.user = current_user

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
