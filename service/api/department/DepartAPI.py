# -*- coding:utf-8 -*-
"""
@project : CCMS
@author:hyongchang
@file:DepartAPI.py
@ide: PyCharm
@time: 2020-09-23 21:27
"""
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import requests
from config.config import HOST
from service.api.common.UserApi import login
from config.config import admin_login_payload

# 公司部门操作
class Department:


    def __init__(self,cookies):
        self.cookies = cookies

    # 增加部门
    def add_depart(self,payload,ret_json=True):
        url = f"{HOST}/api/v4/organizations"
        response = requests.post(url=url,json=payload,cookies=self.cookies)
        if ret_json:
            return response.json()
        return response.json()["value"]

    # 删除所有部门信息
    def del_all_depart(self):
        for depart in self.list_depart()[1:]:
            if "children" in depart and depart["children"]:
                for depart_id in depart["children"]:
                    self.del_depart(depart_id)
            else:
                self.del_depart(depart["_id"])

    def del_depart(self,organization_id):
        """
        删除部门
        :param organization_id: 部门id
        :return:
        """
        url = f"{HOST}/api/v4/organizations/{organization_id}"
        response = requests.delete(url=url,cookies=self.cookies)
        return response.json()

    def modify_depart(self,organization_id,payload):
        """
        修改部门
        :param organization_id:部门id
        :param payload:修改部门信息
        :return:
        """
        url = f"{HOST}/api/v4/organizations/{organization_id}"
        response = requests.put(url=url,json=payload,cookies=self.cookies)
        return response.json()

    def list_depart(self,ret_departs=True):
        url = f"{HOST}/api/v4/organizations"
        response = requests.get(url=url,cookies=self.cookies)
        if ret_departs:
            return response.json()["value"]
        return response.json()

depart = Department(login(admin_login_payload))

if __name__ == '__main__':
    from service.api.common.UserApi import login
    from config.config import admin_login_payload
    depart = Department(login(admin_login_payload))
    list_depart = depart.list_depart()
    print(list_depart)
    # depart.del_all_depart()
    parent = list_depart[0]["company_id"]
    space = list_depart[0]["space"]
    payload = {
                 "name": "上海一部",
                 "parent": parent,
                 "sort_no": 101,
                 "hidden": False,
                 "space": space
            }
    print(depart.add_depart(payload=payload))
    payload = {
        "$set": {
            "name": "testccc",
            "parent": parent,
            "sort_no": 100,
            "hidden": False,
            "space": space
        }
    }
    print(depart.modify_depart(list_depart[2]["_id"],payload))




