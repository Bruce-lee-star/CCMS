# -*- coding:utf-8 -*-
"""
@author:hyongchang
@file:conftest.py
@time:2020/07/14
"""
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import pytest, allure
from service.api.Business.Business import org

@pytest.fixture(scope="session")
def init_no_org():
    with allure.step("初始化删除所有部门信息"):
        org.delete_all()
        yield
        with allure.step("销毁删除所有部门"):
            org.delete_all()
