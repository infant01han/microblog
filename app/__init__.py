# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 0025 8:58
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
# app.config['SECRET_KEY'] = "I am a secret, you can't guess."
app.config.from_object(Config)
db = SQLAlchemy(app)#数据库对象
migrate = Migrate(app, db)#迁移引擎对象
login = LoginManager(app)

from app import routes,models # 这里要写在app后面