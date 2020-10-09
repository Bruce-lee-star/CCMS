# -*- coding:utf-8 -*-
"""
@author:hyongchang
@file:config.py
@time:2020/07/11
"""
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import yaml

class YamlUtils():
    @staticmethod
    def read_yml(path):
        with open(path, encoding='utf8') as f:
            content = yaml.safe_load(f)
        return content

    @staticmethod
    def write_yml(path, data):
        with open(path, 'w', encoding='utf8') as f:
            yaml.safe_dump(data, f, allow_unicode=True)