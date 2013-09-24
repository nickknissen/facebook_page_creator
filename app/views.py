from flask import render_template, flash, redirect, url_for
from flask.ext.login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, \
    check_password_hash
from app import app, lm
from app.forms import LoginForm
from app.models import User, db

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('pages'))
    form = LoginForm()
    if form.validate_on_submit():
        flash('error validating')
        return redirect('/index')
    return render_template('login.html', 
        title = 'Log ind',
        form = form)

@login_required
@app.route('/pages')
def pages():
    return render_template('pages.html')

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


def validate_user(email, password, remember_me=None):
    if email and password:
        user = User.find_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                if remember_me:
                    remember = None
                else:
                    remember = True

                login_user(user, remember=remember)
                return user

def create_user(email, password):
    user = User(email, generate_password_hash(password))
    db.session.add(user)
    db.session.commit()