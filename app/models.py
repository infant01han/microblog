# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 0025 14:08
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : models.py
# @Software: PyCharm
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    def set_password(self,passwd):
        self.password_hash = generate_password_hash(passwd)
    def check_password(self,passwd):
        return check_password_hash(self.password_hash,passwd)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}'.format(self.body)