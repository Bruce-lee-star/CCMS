# -*- coding:utf-8 -*-
"""
@project : CCMS
@author:hyongchang
@file:Business.py
@ide: PyCharm
@time: 2020-09-26 12:06
"""
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from service.api.common.BaseApi import BaseApi


class OrganizationAPI(BaseApi):

    def __init__(self):
        super().__init__()

    def delete_all(self):
        for org in self.list():
            self.delete(org["_id"])

    def get_parent(self):
        """
        获得当前公司的id属性值
        :return:
        """
        return self.list()[0]["_id"]


class AccountsAPI(BaseApi):
    pass


class ContractTypesAPI(BaseApi):
    pass

class ContractAPI(BaseApi):
    pass


# 公司部门实例
org = OrganizationAPI()
# 签约对象实例
accounts = AccountsAPI()
# 合同类型
contractType = ContractTypesAPI()
# 合同
contract = ContractAPI()


