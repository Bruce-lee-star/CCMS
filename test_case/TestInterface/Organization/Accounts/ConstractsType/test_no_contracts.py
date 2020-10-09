# -*- coding:utf-8 -*-
"""
@project : CCMS
@author:hyongchang
@file:test_no_contracts.py
@ide: PyCharm
@time: 2020-09-27 23:10
"""
import sys
import os

import allure
import pytest
from random import randint
from service.api.Business.Business import contract
from utils.CommonUtils.DateUtils import DateUtils

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

@allure.feature("当前系统没有合同")
class TestContracts():

    def setup_class(self):
        self.payload = {
            "$top": 50,
            "$select": "name,phone,address,company_id",
            "$count": "true"
        }

    @pytest.fixture()
    def after_tc003001(self,init_no_contracts):
        yield
        with allure.step("后置操作：删除创建的合同"):
            contract.delete(self.ret_add_contract["_id"])

    @allure.story("创建合同")
    @pytest.mark.usefixtures("after_tc003001")
    def test_tc003001(self,init_accounts_data,init_contract_type_data,init_org_data):
        accounts_id = init_accounts_data
        contract_type_id = init_contract_type_data
        org_id = init_org_data
        with allure.step("添加合同"):
            self.ret_add_contract = contract.add(no=f"合同{randint(111111,999999)}",
                                                 create_date=DateUtils.get_current_time(),company_id=org_id,
                                                 othercompany=accounts_id,contract_type=contract_type_id,
                                                 name="付款合同")
            ret_list_contract = contract.list(self.payload)
            for contract_one in ret_list_contract:
                if self.ret_add_contract["_id"] == contract_one["_id"]:
                    assert "付款合同" == contract_one["name"]
                    break

    @allure.story("修改id不存在的合同")
    @pytest.mark.usefixtures("init_no_contracts")
    def test_tc003052(self):
        ret_list_contract_before = contract.list()
        contract.modify("test_modify",name="汽车销售合同")
        ret_modify_contract = ret_list_contract_after = contract.list()
        print(ret_modify_contract)
        assert ret_list_contract_before == ret_list_contract_after

    @pytest.fixture()
    def before_tc003091(self,init_no_contracts,init_accounts_data,init_contract_type_data,init_org_data):
        accounts_id = init_accounts_data
        contract_type_id = init_contract_type_data
        org_id = init_org_data
        with allure.step("前置操作：创建合同"):
            ret_add_contract_id = contract.add(no=f"合同{randint(111111, 999999)}", create_date=DateUtils.get_current_time(),
                                               company_id=org_id, othercompany=accounts_id,
                                               contract_type=contract_type_id, name="购物合同")["_id"]
            return ret_add_contract_id

    @allure.story("删除id存在的合同")
    @pytest.mark.usefixtures("before_tc003091")
    def test_tc003091(self,before_tc003091):
        ret_add_contract_id = before_tc003091
        contract.delete(ret_add_contract_id)
        assert contract.list() == []

