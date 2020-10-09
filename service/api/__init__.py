# -*- coding:utf-8 -*-
"""
@author:hyongchang
@file:__init__.py.py
@time:2020/07/11
"""
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)