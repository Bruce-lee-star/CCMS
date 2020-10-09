# -*- coding:utf-8 -*-
"""
@project : CCMS
@author:hyongchang
@file:BaseApi.py
@ide: PyCharm
@time: 2020-09-26 10:04
"""
import sys
import os
import requests
from config.config import HOST,admin_login_payload
from service.api.common.UserApi import User
from utils.CommonUtils.YamlUtils import YamlUtils
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


class BaseApi:

    def __init__(self,cookies=None):
        # 获取当前继承基类的名称
        self.class_name = self.__class__.__name__
        # 获取当前类的API配置模板信息
        self.current_cfg = YamlUtils().read_yml(f"{sys.path[0]}/config/api_conf.yml")[self.class_name]
        # 获取URL
        self.url = self.current_cfg["url"]
        if cookies:
            # 正式测试的时候，需要统一cookies
            self.cookies = cookies
        else:
            # 用于临时测试产生cookies
            self.cookies = User.login(admin_login_payload)
        self.space_id = self.cookies["X-Space-Id"]

    def add(self, **kwargs):
        """
        增加
        :param kwargs:
        :return:
        """
        payload = self.current_cfg["add"]
        payload.update(kwargs)
        payload["space"] = self.space_id
        response = requests.post(url=f"{HOST}{self.url}",json=payload,cookies=self.cookies)
        if "value" in response.json():
            return response.json()["value"][0]
        return response.json()

    def delete(self,_id):
        """
        删除
        :param _id:
        :return:
        """
        response = requests.delete(url=f"{HOST}{self.url}/{_id}",cookies=self.cookies)
        return response.json()

    def modify(self,_id,**kwargs):
        """
        修改
        :param _id:
        :param kwargs:
        :return:
        """
        payload = self.current_cfg["modify"]
        payload["$set"].update(kwargs)
        payload["$set"]["space"] = self.space_id
        response = requests.put(url=f"{HOST}{self.url}/{_id}", json=payload, cookies=self.cookies)
        return response.json()

    def list(self,payload=None):
        """
        查询
        :param payload: 查询参数
        :return:
        """
        if payload:
            response = requests.get(url=f"{HOST}{self.url}", json=payload, cookies=self.cookies)
        else:
            response = requests.get(url=f"{HOST}{self.url}", cookies=self.cookies)
        return response.json()["value"]

    def delete_all(self,payload=None):
        """
        删除所有
        :param payload: 查询参数
        :return:
        """
        if payload:
            while 1:
                for one in self.list(payload=payload):
                    self.delete(one["_id"])
                else:
                    break
        else:
            for one in self.list():
                self.delete(one["_id"])

