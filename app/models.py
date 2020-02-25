# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 0025 14:08
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : models.py
# @Software: PyCharm
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)