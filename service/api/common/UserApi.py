# -*- coding:utf-8 -*-
"""
@project : CCMS
@author:hyongchang
@file:UserApi.py
@ide: PyCharm
@time: 2020-09-22 23:15
"""
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import requests
from config.config import HOST

class User():
    # 用户登录操作
    @classmethod
    def login(self, payload, return_cookies=True):
        url = f"{HOST}/accounts/password/authenticate"
        response = requests.post(url=url, json=payload)
        if return_cookies:
            return response.cookies
        else:
            return response.text
    # 用户认证操作
    @classmethod
    def auther(self,cookies):
        url = f"{HOST}/accounts/user"
        response = requests.get(url=url,cookies=cookies)
        return response.json()

    # 用户注册操作
    @classmethod
    def resister(self, payload):
        url = f"{HOST}/accounts/password/register"
        response = requests.post(url,json=payload)
        return response.json()
if __name__ == '__main__':
    from config.config import admin_login_payload
    print(User.login(admin_login_payload))
    print(User.login(admin_login_payload,return_cookies=False))
