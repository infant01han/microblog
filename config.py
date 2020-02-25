# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 0025 10:24
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : config.py
# @Software: PyCharm
import os

basedir = os.path.abspath(os.path.dirname(__file__))#获取当前.py文件的绝对路径
class Config:
    SECRET_KEY = os.environ.get('SECRET KEY') or 'you will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False