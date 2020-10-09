# -*- coding:utf-8 -*-
"""
@project : teachMS
@author:hyongchang
@file:__init__.py.py
@ide: PyCharm
@time: 2020-08-30 20:57
"""
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

