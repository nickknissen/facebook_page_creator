#-*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for, request
from flask.ext.login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, lm
from app.forms import LoginForm, ContentForm
from app.models import User, db, Content


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Forside")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('pages'))
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        remember_me = form.remember_me.data
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=remember_me)

                return redirect(url_for('pages'))
        else:
            flash(u'kunne ikke finde brugeren')
            return render_template('login.html', title='Log ind', form=form)
    return render_template('login.html', title='Log ind', form=form)


@app.route('/page/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def page_edit(id):
    content = Content.query.filter_by(id=id).first()
    form = ContentForm()
    if form.validate_on_submit():
        content = Content.query.filter_by(id=id).first()
        content.body = form.body.data
        content.title = form.title.data
        db.session.commit()
    else:
        form.title.data = content.title
        form.body.data = content.body

    return render_template('page/edit.html', title="Side redigering", content=content, form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/page/list')
@login_required
def pages():
    return render_template('page/list.html', title=u"Side håndtering")


@app.route('/preview/<int:id>')
def preview(id):
    content = Content.query.filter_by(id=id).first()
    return render_template('page/preview.html', content=content)


@app.route('/page/<int:id>')
def page(id):
    content = Content.query.filter_by(id=id).first()
    return render_template('page/page.html', content=content)


@app.route('/page/create')
@login_required
def page_create():
    page = Content(title=u"Ny side", body=u"Noget indhold her")
    db.session.add(page)
    db.session.commit()
    return redirect(url_for("page_edit", id=page.id))





@app.route('/user/list')
@login_required
def users():
    return render_template('user/list.html')

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.context_processor
def sidebar_pages():
    pages = Content.query.all()
    return dict(side_content=pages)



def create_user(email, password):
    user = User(email, generate_password_hash(password))
    db.session.add(user)
    db.session.commit()


def delete_content(id):
    content = Content.query.filter_by(id=id).first()
    db.session.delete(content)
    db.session.commit()

def update_content():
    pass