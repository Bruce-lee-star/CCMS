# -*- coding:utf-8 -*-
"""
@project : CCMS
@author:hyongchang
@file:conftest.py
@ide: PyCharm
@time: 2020-09-24 21:36
"""
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import pytest,allure
from service.api.Business.Business import org,accounts

payload = {
        "$top": 50,
        "$select": "name,phone,address,company_id",
        "$count": "true"
    }

@pytest.fixture(scope="session")
def init_org_data(init_no_org):
    with allure.step("初始化创建一个部门"):
        org_id = org.add(name="财务部",parent=org.get_parent())["_id"]
        yield org_id
        with allure.step("销毁删除所有部门"):
            org.delete(org_id)

@pytest.fixture(scope="package")
def init_no_accounts():
    with allure.step("初始化删除所有签约对象信息"):
        accounts.delete_all(payload)
        yield
        with allure.step("销毁删除所有签约对象信息"):
            accounts.delete_all(payload)

