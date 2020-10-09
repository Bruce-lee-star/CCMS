# -*- coding:utf-8 -*-
"""
@project : CCMS
@author:hyongchang
@file:test_organization.py
@ide: PyCharm
@time: 2020-09-26 16:55
"""
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import pytest,allure
from service.api.Business.Business import org

@allure.feature("当前公司已经有分部")
class TestOrg():

    @pytest.fixture()
    def after_tc000001(self):
        yield
        org.delete(self.ret_add_org["_id"])

    @allure.story("创建一个新的部门")
    @pytest.mark.usefixtures("after_tc000001")
    @pytest.mark.usefixtures("init_org_data")
    def test_tc000001(self):
        allure.step("创建一个新的部门")
        self.ret_add_org = org.add(name="生产质量部",parent = org.get_parent())
        ret_list_org = org.list()
        assert self.ret_add_org in ret_list_org

    @allure.story("修改id存在的部门")
    def test_tc000051(self,init_org_data):
        org_id = init_org_data
        allure.step("修改id存在的部门")
        org.modify(org_id,name="软件实施部",parent=org.get_parent())
        for org_one in org.list():
            if org_id == org_one["_id"]:
                assert "软件实施部" == org_one["name"]
                break

    @allure.story("修改id不存在的部门")
    @pytest.mark.usefixtures("init_org_data")
    def test_tc000052(self):
        allure.step("修改id不存在的部门")
        org.modify("test001x",name="人力资源部",parent=org.get_parent())
        for org_one in org.list():
            assert "人力资源部" != org_one["name"]

    @allure.story("删除不存在的id")
    def test_tc000092(self):
        ret_org_list_before = org.list()
        org.delete("test002z")
        ret_org_list_after = org.list()
        assert ret_org_list_before == ret_org_list_after