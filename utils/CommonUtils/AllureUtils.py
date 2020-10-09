#-*- coding: UTF-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import allure
from functools import wraps


class AllureUtils:

    @staticmethod
    def dynamic_title(target):
        def decrorate(func):
            @wraps(func) # 保留原函数名称
            def warppper(*args, **kwargs):
                func(*args, **kwargs)
                if target in kwargs:
                    allure.dynamic.title(kwargs[target])
                else:
                    allure.dynamic.title(target)
            return warppper
        return decrorate

    @staticmethod
    def dynamic_story(target):
        def decrorate(func):
            @wraps(func)  # 保留原函数名称
            def warppper(*args, **kwargs):
                func(*args, **kwargs)
                if target in kwargs:
                    allure.dynamic.story(kwargs[target])
                else:
                    allure.dynamic.story(target)
            return warppper
        return decrorate

    @staticmethod
    def dynamic_description(target):
        def decrorate(func):
            @wraps(func)  # 保留原函数名称
            def warppper(*args, **kwargs):
                func(*args, **kwargs)
                if target in kwargs:
                    allure.dynamic.description(kwargs[target])
                else:
                    allure.dynamic.description(target)
            return warppper
        return decrorate

    @staticmethod
    def dynamic_issue(target):
        def decrorate(func):
            @wraps(func)  # 保留原函数名称
            def warppper(*args, **kwargs):
                func(*args, **kwargs)
                if target in kwargs:
                    allure.dynamic.issue(kwargs[target])
                else:
                    allure.dynamic.issue(target)
            return warppper
        return decrorate

