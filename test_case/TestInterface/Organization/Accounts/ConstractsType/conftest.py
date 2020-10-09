# -*- coding:utf-8 -*-
"""
@project : CCMS
@author:hyongchang
@file:conftest.py
@ide: PyCharm
@time: 2020-09-27 19:46
"""
import sys
import os

import allure

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import pytest
from service.api.Business.Business import contractType,contract

payload = {
        "$top": 50,
        "$select": "name,phone,address,company_id",
        "$count": "true"
    }

@pytest.fixture(scope="package")
def init_contract_type_data():
    with allure.step("fixture前置操作：增加合同类型"):
        contract_type_id = contractType.add(name="手机出租合同",code="SJ20200927005")["_id"]
        yield contract_type_id
        with allure.step("fixture后置操作：删除合同类型"):
            contractType.delete(contract_type_id)

@pytest.fixture(scope="package")
def init_no_contracts():
    with allure.step("fixture前置操作：删除所有合同"):
        contract.delete_all(payload)
        yield
        with allure.step("fixture后置操作：删除所有合同"):
            contract.delete_all(payload)

