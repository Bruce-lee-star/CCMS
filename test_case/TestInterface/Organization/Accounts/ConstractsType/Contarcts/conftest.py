# -*- coding:utf-8 -*-
"""
@project : CCMS
@author:hyongchang
@file:conftest.py
@ide: PyCharm
@time: 2020-09-28 22:25
"""
import sys
import os
from random import randint

import pytest,allure
from service.api.Business.Business import contract
from utils.CommonUtils.DateUtils import DateUtils

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


@pytest.fixture(scope="package")
def init_contract_data(init_accounts_data,init_contract_type_data,init_org_data):
    accounts_id = init_accounts_data
    contract_type_id = init_contract_type_data
    org_id = init_org_data
    with allure.step("fixture前置：创建合同"):
        ret_add_contract_id = contract.add(no=f"合同{randint(111111,999999)}",create_date=DateUtils.get_current_time(),
                                        company_id=org_id,othercompany=accounts_id,
                                        contract_type=contract_type_id,name="购车合同")["_id"]
        yield ret_add_contract_id
        with allure.step("fixture后置：删除合同"):
            contract.delete(ret_add_contract_id)
