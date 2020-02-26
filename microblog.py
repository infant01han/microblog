# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 0025 9:03
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : microblog.py
# @Software: PyCharm
import logging

from app import app


app.logger.setLevel(logging.INFO)
app.logger.info('Microblog startup')  # 在有可能出现问题的地方加这行代码，可以生成日志
app.run()