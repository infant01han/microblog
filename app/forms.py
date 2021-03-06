# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 0025 10:34
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : forms.py
# @Software: PyCharm

from flask_wtf import FlaskForm#从flask_wtf包中导入FlaskForm类
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField  # 导入这些类
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length

from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About_me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self,username):
        super().__init__()
        self.old_username = username

    def validate_username(self,username):
        if username.data != self.old_username:
            user = User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError('用户名已存在，请重新输入')

class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')