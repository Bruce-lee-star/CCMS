# -*- coding:utf-8 -*-
"""
@project : CCMS
@author:hyongchang
@file:test_no_organization.py
@ide: PyCharm
@time: 2020-09-26 15:53
"""
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import pytest,allure
from service.api.Business.Business import org


@allure.feature("当前公司没有分部")
class TestNoOrg():

    @pytest.fixture()
    def after_tc000001(self,init_no_org):
        yield
        with allure.step("删除创建的分部信息"):
            org.delete(self.ret_add_org["_id"])

    @allure.story("创建分部")
    @pytest.mark.usefixtures("after_tc000001")
    def test_tc000001(self):
        self.ret_add_org = org.add(name="市场营销部",parent=org.get_parent())
        ret_list_org = org.list()
        assert self.ret_add_org in ret_list_org

    @pytest.fixture()
    def create_org(self):
        with allure.step("创建分部"):
            ret_org_id = org.add(name="研发部",parent=org.get_parent())["_id"]
            return ret_org_id

    @pytest.mark.usefixtures("init_no_org")
    def test_tc000091(self, create_org):
        ret_org_id = create_org
        with allure.step("删除分部"):
            org.delete(ret_org_id)
            ret_list_org_after = org.list()[1:]
            assert ret_list_org_after == []

