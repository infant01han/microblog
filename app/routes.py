# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 0025 9:01
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : routes.py
# @Software: PyCharm
from datetime import datetime
from hashlib import md5

from flask import render_template, flash, redirect, url_for, session, request
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm, PostForm
from app.models import User, Post


# 拦截器
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/')
@app.route('/index',methods=['GET','POST'])
@login_required
def index():
    form = PostForm()
    # usr = {'username':'zhangsan'}
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    page = request.args.get('page',1,type=int)
    posts = current_user.followed_posts().paginate(page,app.config['POSTS_PER_PAGE'],False)
    next_url = url_for('index',page=posts.next_num) if posts.has_next else None
    prev_url = url_for('index',page=posts.prev_num) if posts.has_prev else None
    return render_template('index.html',title='home',form=form,posts=posts.items,next_url=next_url,prev_url=prev_url)

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user,remember=form.remember_me.data)

        # 重定向到 next 页面，从哪里跳到登录页面的回到哪里去
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            return redirect(url_for('index'))
        return redirect(next_page)

    return render_template('login.html',title='login',form=form)

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)
# @app.route('/hello')
# def hello():
#     session['username']='lisi'
#     return 'hello'

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(user_id=user.id).order_by(Post.timestamp.desc()).paginate(page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('user', username=user.username, page=posts.next_num) if posts.has_next else None
    prev_url = url_for('user', username=user.username, page=posts.prev_num) if posts.has_prev else None
    return render_template('user.html',user=user,posts=posts.items,next_url=next_url, prev_url=prev_url)

@app.route('/edit_profile',methods=['GET','POST'])
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        # flash('success')
        return redirect(url_for('user',username=current_user.username))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html',title='edit_profile',form=form)

@app.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return redirect(url_for('index'))
    if user == current_user:
        return redirect(url_for('user',username=username))
    current_user.follow(user)
    db.session.commit()
    return redirect(url_for('user',username=username))

@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return redirect(url_for('index'))
    if user == current_user:
        return redirect(url_for('user',username=username))
    current_user.unfollow(user)
    db.session.commit()
    return redirect(url_for('user',username=username))

@app.route('/explore')
@login_required
def explore():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('explore', page=posts.next_num) if posts.has_next else None
    prev_url = url_for('explore', page=posts.prev_num) if posts.has_prev else None
    return render_template('/index.html',title='Explore',posts=posts.items,next_url=next_url, prev_url=prev_url)