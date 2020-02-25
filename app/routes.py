# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 0025 9:01
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : routes.py
# @Software: PyCharm
from flask import render_template

from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    usr = {'username':'zhangsan'}
    posts = [#创建一个列表：帖子。里面元素是两个字典，每个字典里元素还是字典，分别作者、帖子内容。
        {
            'author': {'username':'John'},
            'body':'Beautiful day in Portland!'
        },
        {
            'author': {'username':'Susan'},
            'body':'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',title='home',user=usr,posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title='login',form=form)