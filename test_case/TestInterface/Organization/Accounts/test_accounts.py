# -*- coding:utf-8 -*-
"""
@project : CCMS
@author:hyongchang
@file:test_accounts.py
@ide: PyCharm
@time: 2020-09-26 18:47
"""
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import pytest,allure
from service.api.Business.Business import accounts
from utils.CommonUtils.AllureUtils import AllureUtils


@allure.feature("当前公司已经存在签约对象")
class TestAccounts():

    def setup_class(self):
        self.payload = {
                        "$top": 50,
                        "$select": "name,phone,address,company_id",
                        "$count": "true"
                    }

    # @allure.story("创建新的签约对象")
    @AllureUtils.dynamic_title("创建新的签约对象")
    @pytest.mark.usefixtures("init_accounts_data")
    def test_tc001002(self,init_org_data):
        org_id = init_org_data
        with allure.step("创建新的签约对象"):
            ret_add_accounts = accounts.add(name="拼多多",category="1",company_ids=[org_id])
            for accounts_one in accounts.list(self.payload):
                if ret_add_accounts["_id"] == accounts_one["_id"]:
                    assert "拼多多" == accounts_one["name"]
                    break

    # @allure.story("修改id存在签约对象")
    @AllureUtils.dynamic_title("修改id存在签约对象")
    def test_tc001051(self,init_accounts_data):
        accounts_id = init_accounts_data
        allure.step("修改id存在签约对象")
        accounts.modify(accounts_id,name="京东物流")
        for accounts_one in accounts.list(self.payload):
            if accounts_id == accounts_one["_id"]:
                assert "京东物流" == accounts_one["name"]
                break

    # @allure.story("删除id不存在的签约对象")
    @AllureUtils.dynamic_title("删除id不存在的签约对象")
    @pytest.mark.usefixtures("init_accounts_data")
    def test_tc001092(self):
        ret_list_account_before = accounts.list(self.payload)
        accounts.delete("test_delete")
        ret_list_account_after = accounts.list(self.payload)
        assert ret_list_account_before == ret_list_account_after

