# -*- coding:utf-8 -*-
"""
@project : CCMS
@author:hyongchang
@file:conftest.py
@ide: PyCharm
@time: 2020-09-26 18:05
"""
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import pytest,allure
from service.api.Business.Business import accounts,contractType

payload = {
        "$top": 50,
        "$select": "name,phone,address,company_id",
        "$count": "true"
    }

@pytest.fixture(scope="package")
def init_accounts_data(init_no_accounts,init_org_data):
    with allure.step("fixture前置操作：创建一个签约对象"):
        accounts_id = accounts.add(name="京东集团",category=1,company_ids=[init_org_data])["_id"]
        yield accounts_id
        with allure.step("fixture后置操作：删除前置创建的签约对象"):
            accounts.delete(accounts_id)

@pytest.fixture(scope="package")
def init_constract_types():
    with allure.step("fixture前置操作：删除所有的合同类型"):
        contractType.delete_all(payload)
        yield
        with allure.step("fixture后置操作：删除所有的合同类型"):
            contractType.delete_all(payload)