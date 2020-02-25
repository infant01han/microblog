# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 0025 10:34
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : forms.py
# @Software: PyCharm

from flask_wtf import FlaskForm#从flask_wtf包中导入FlaskForm类
from wtforms import StringField,PasswordField,BooleanField,SubmitField#导入这些类
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')