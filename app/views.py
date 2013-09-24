from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('error validating')
        return redirect('/index')
    return render_template('login.html', 
        title = 'Sign In',
        form = form)