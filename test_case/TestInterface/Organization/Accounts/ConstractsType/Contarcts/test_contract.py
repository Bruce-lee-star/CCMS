# -*- coding:utf-8 -*-
"""
@project : CCMS
@author:hyongchang
@file:test_contract.py
@ide: PyCharm
@time: 2020-09-28 22:29
"""
import sys
import os
from random import randint

import allure
import pytest

from service.api.Business.Business import contract
from utils.CommonUtils.DateUtils import DateUtils
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

@allure.feature("当前系统有合同")
class TestContract():

    @pytest.fixture()
    def before_tc003002(self,init_contract_data):
        yield
        with allure.step("后置操作：删除创建的合同"):
            contract.delete(self.ret_add_contract["_id"])

    @allure.story("创建合同")
    @pytest.mark.usefixtures("before_tc003002")
    def test_tc003002(self,init_accounts_data,init_contract_type_data,init_org_data):
        accounts_id = init_accounts_data
        contract_type_id = init_contract_type_data
        org_id = init_org_data
        with allure.step("创建合同"):
            self.ret_add_contract = contract.add(no=f"合同{randint(111111, 999999)}", create_date=DateUtils.get_current_time(),
                                               company_id=org_id, othercompany=accounts_id,
                                               contract_type=contract_type_id, name="购房合同")
            for contract_one in contract.list():
                if self.ret_add_contract["_id"] == contract_one["_id"]:
                    assert self.ret_add_contract["name"] == contract_one["name"]
                    break

    @allure.story("修改id存在的合同")
    def test_tc003051(self,init_contract_data):
        contract_id = init_contract_data
        contract.modify(contract_id,name="罚款合同")
        for contract_one in contract.list():
            if contract_id == contract_one["_id"]:
                assert "罚款合同" == contract_one["name"]
                break

    @allure.story("修改id不存在的合同")
    @pytest.mark.usefixtures("init_contract_data")
    def test_tc003092(self):
        ret_list_contract_before = contract.list()
        contract.delete("test_delete")
        ret_list_contract_after = contract.list()
        assert ret_list_contract_before == ret_list_contract_after