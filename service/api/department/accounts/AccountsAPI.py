# -*- coding:utf-8 -*-
"""
@project : CCMS
@author:hyongchang
@file:AccountsAPI.py
@ide: PyCharm
@time: 2020-09-24 23:27
"""
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import requests
from config.config import HOST,admin_login_payload
from service.api.common.UserApi import login
class AccountsApi():

    def __init__(self, cookies):
        self.cookies = cookies

    def add_accounts(self,payload,ret_json=True):
        url = f"{HOST}/api/v4/accounts"
        response = requests.post(url=url,json=payload,cookies=self.cookies)
        if ret_json:
            return response.json()
        return response.json()["value"]

    def del_accounts(self,account_id):
        url = f"{HOST}/api/v4/accounts/{account_id}"
        response = requests.delete(url,cookies=self.cookies)
        return response.json()

    def del_all_accounts(self):
        payload = {
            "$top" : 50,
            "$select" : "name,phone,address,company_id",
            "$count"  : "true"
        }
        while 1:
            for account in self.list_accounts(payload):
                self.del_accounts(account["_id"])
            else:
                break

    def modify_accounts(self,account_id,payload):
        url = f"{HOST}/api/v4/accounts/{account_id}"
        response = requests.put(url=url,json=payload,cookies=self.cookies)
        return response.json()

    def list_accounts(self,payload,ret_accounts=True):
        url = f"{HOST}/api/v4/accounts"
        response = requests.get(url=url,json=payload,cookies=self.cookies)
        if ret_accounts:
            return response.json()["value"]
        return response.json()

account = AccountsApi(login(admin_login_payload))

if __name__ == '__main__':
    from service.api.department.DepartAPI import depart

    list_depart = depart.list_depart()
    parent = list_depart[0]["company_id"]
    space = list_depart[0]["space"]
    payload = {
        "name": "上海一部",
        "parent": parent,
        "sort_no": 101,
        "hidden": False,
        "space": space
    }
    depart_id = depart.add_depart(payload,ret_json=False)[0]["_id"]

    account.del_all_accounts()
    payload = {
        "name": "name",
        "category": 1,
        "company_ids": [depart_id],
        "status": 1,
        "space": space
    }

    account_id = account.add_accounts(payload,ret_json=False)[0]["_id"]
    payload = {
            "$set": {
                "name": "testobj001",
                "phone": "400-888888",
                "address": "南京市软件大道",
                "registered_capital": 1000000,
                "category": "1",
                "credit_code": "370202199507078632",
                "company_ids": [depart_id],
                "status": "2",
                "space": "jTaQzFyri4ojvYSQm"
               }
            }
    print(account.modify_accounts(account_id,payload))
    payload = {
        "$top": 50,
        "$select": "name,phone,address,company_id",
        "$count": "true"
    }
    print(account.list_accounts(payload))

