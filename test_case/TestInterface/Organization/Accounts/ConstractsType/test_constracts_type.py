# -*- coding:utf-8 -*-
"""
@project : CCMS
@author:hyongchang
@file:test_constracts_type.py
@ide: PyCharm
@time: 2020-09-27 19:45
"""
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import pytest,allure
from service.api.Business.Business import contractType

@allure.feature("当前系统已有合同类型")
class TestContractsType():

    def setup_class(self):
        self.payload = {
            "$top": 50,
            "$select": "name,phone,address,company_id",
            "$count": "true"
        }

    @pytest.fixture()
    def after_tc002002(self):
        yield
        with allure.step("后置操作：删除创建的合同类型"):
            contractType.delete(self.ret_add_contract_type["_id"])

    @allure.story("创建合同")
    @pytest.mark.usefixtures("after_tc002002")
    @pytest.mark.usefixtures("init_contract_type_data")
    def test_tc002002(self):
        with allure.step("创建合同"):
            self.ret_add_contract_type = contractType.add(name="笔记本售卖合同",code="BJB20200917520")
            for contract_type in contractType.list(self.payload):
                if self.ret_add_contract_type["_id"] == contract_type["_id"]:
                    assert "笔记本售卖合同" == contract_type["name"]
                    break
    @allure.story("修改id存在的合同")
    def test_tc002051(self,init_contract_type_data):
        contract_type_id = init_contract_type_data
        contractType.modify(contract_type_id,name="房屋出租合同")
        for contract_type in contractType.list(self.payload):
            if contract_type_id == contract_type["_id"]:
                assert "房屋出租合同" == contract_type["name"]
                break

    @allure.story("删除id不存在的合同")
    @pytest.mark.usefixtures("init_contract_type_data")
    def test_tc002092(self):
        ret_list_contract_type_before = contractType.list(self.payload)
        contractType.delete("test_midify")
        ret_list_contract_type_after = contractType.list(self.payload)
        assert ret_list_contract_type_before == ret_list_contract_type_after