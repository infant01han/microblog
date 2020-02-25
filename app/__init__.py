# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 0025 8:58
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Flask

from config import Config

app = Flask(__name__)
# app.config['SECRET_KEY'] = "I am a secret, you can't guess."
app.config.from_object(Config)
from app import routes  # 这里要写在app后面