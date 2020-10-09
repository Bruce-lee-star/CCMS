# -*- coding:utf-8 -*-
"""
@project : CCMS
@author:hyongchang
@file:conftest.py
@ide: PyCharm
@time: 2020-10-08 19:59
"""
import sys
import os

import allure
import pytest

from service.webui.Business import LoginPage

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


@pytest.fixture(scope="session")
def init_browser():
    with allure.step("打开浏览器"):
        login = LoginPage()
    yield login
    with allure.step("关闭浏览器"):
        login.close_browser()
