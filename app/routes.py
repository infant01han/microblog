# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 0025 9:01
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : routes.py
# @Software: PyCharm
from app import app


@app.route('/')
def index():
    return 'hello'