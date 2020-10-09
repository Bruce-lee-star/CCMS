# -*- coding:utf-8 -*-
"""
@project : CCMS
@author:hyongchang
@file:test_no_constracts_type.py
@ide: PyCharm
@time: 2020-09-26 22:14
"""
import sys
import os

import allure

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import pytest
from service.api.Business.Business import contractType

@allure.feature("当前公司没有合同类型")
class TestConstractsNoType():

    def setup_class(self):
        self.payload = {
            "$top": 50,
            "$select": "name,phone,address,company_id",
            "$count": "true"
        }

    @pytest.fixture()
    def after_tc002001(self):
        yield
        with allure.step("后置操作：删除创建的合同类型"):
            contractType.delete(self.ret_add_contract_type["_id"])
    @allure.story("增加名称不同的合同类型")
    @pytest.mark.usefixtures("after_tc002001")
    @pytest.mark.usefixtures("init_constract_types")
    def test_tc002001(self):
        with allure.step("增加合同类型"):
            self.ret_add_contract_type = contractType.add(name="出租合同",code="CZ20200925001")
            ret_list_contract_type = contractType.list(self.payload)
            for contract_type in ret_list_contract_type:
                if self.ret_add_contract_type["_id"] == contract_type["_id"]:
                    assert self.ret_add_contract_type["name"] == contract_type["name"]
                    break
    @allure.story("删除id不存在的合同类型")
    def test_tc002052(self):
        contractType.modify("test_contract",name="买卖合同")
        assert contractType.list(self.payload) == []

    @pytest.fixture()
    def before_tc002091(self):
        with allure.step("前置操作：增加合同类型"):
            contract_type_id = contractType.add(name="销售合同",code="XS20200926002")["_id"]
            return contract_type_id

    @allure.story("删除id存在的合同类型")
    def test_tc002091(self,before_tc002091):
        contract_type_id = before_tc002091
        with allure.step("删除合同类型"):
            contractType.delete(contract_type_id)
            print(contractType.list(self.payload))
            assert contractType.list(self.payload) == []

