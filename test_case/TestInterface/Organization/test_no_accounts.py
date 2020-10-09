# -*- coding:utf-8 -*-
"""
@project : CCMS
@author:hyongchang
@file:test_no_accounts.py
@ide: PyCharm
@time: 2020-09-26 17:50
"""
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import pytest,allure
from service.api.Business.Business import accounts

@allure.feature("当前公司没有签约对象")
class TestNoAccounts():

    def setup_class(self):
        with allure.step("初始化payload数据"):
            self.payload = {
                    "$top": 50,
                    "$select": "name,phone,address,company_id",
                    "$count": "true"
                }

    @pytest.fixture()
    def after_tc001001(self,init_no_accounts):
        yield
        with allure.step("销毁添加签约对象的后置操作"):
            accounts.delete(self.ret_add_accounts["_id"])


    @allure.story("添加签约对象")
    @pytest.mark.usefixtures("after_tc001001")
    def test_tc001001(self,init_org_data):
        org_id = init_org_data
        allure.step("添加签约对象")
        self.ret_add_accounts = accounts.add(name="天猫",category=1,company_ids=[org_id])
        ret_list_accounts = accounts.list(self.payload)
        assert self.ret_add_accounts in ret_list_accounts


    @allure.story("修改id不存在签约对象")
    @pytest.mark.usefixtures("init_no_accounts")
    def test_tc001052(self,init_org_data):
        org_id = init_org_data
        allure.step("修改id不存在签约对象")
        accounts.modify("test_modify", name="淘宝",category=1,company_ids=[org_id])
        assert accounts.list(self.payload) == []

    @pytest.fixture()
    def create_accounts(self,init_org_data):
        with allure.step("前置操作-添加签约对象数据"):
            org_id = init_org_data
            accounts_id = accounts.add(name="百度",category=1,company_ids=[org_id])["_id"]
            return accounts_id

    @allure.story("删除id存在的签约对象")
    def test_tc001091(self,create_accounts):
        accounts_id = create_accounts
        accounts.delete(accounts_id)
        ret_list_accounts = accounts.list(self.payload)
        assert ret_list_accounts == []


