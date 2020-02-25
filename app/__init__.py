# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 0025 8:58
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Flask

app = Flask(__name__)
from app import routes  # 这里要写在app后面