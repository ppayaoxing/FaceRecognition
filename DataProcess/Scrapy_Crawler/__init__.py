# encoding: utf-8

"""
@author: liubo-it
@software: PyCharm Community Edition
@file: __init__.py.py
@time: 2016/8/1 13:38
@contact: ustb_liubo@qq.com
@annotation: __init__.py
"""
import sys
import logging
from logging.config import fileConfig
import os

reload(sys)
sys.setdefaultencoding("utf-8")
fileConfig('logger_config.ini')
logger_error = logging.getLogger('errorhandler')

if __name__ == '__main__':
    pass
