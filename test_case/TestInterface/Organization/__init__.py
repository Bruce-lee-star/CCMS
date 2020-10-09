# -*- coding:utf-8 -*-
"""
@project : CCMS
@author:hyongchang
@file:__init__.py.py
@ide: PyCharm
@time: 2020-09-26 15:46
"""
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

