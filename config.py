# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 0025 10:24
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : config.py
# @Software: PyCharm
import os


class Config:
    SECRET_KEY = os.environ.get('SECRET KEY') or 'you will never guess'