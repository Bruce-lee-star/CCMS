# -*- coding:utf-8 -*-
"""
@author:hyongchang
@file:ReadTabDataUtils.py
@time:2020/07/05
"""
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from utils.ApiUtils.XlrdUtils import XlrdUtils
import json

# 满足定制化需求
def read_test_data(xl_path, sheet_index_or_name = None, row_num = None, *cols_index):
    """
    :param xl_path: xls文件路径
    :param sheet_index_or_name: sheet页的索引或名称
    :param row_num: 获取sheet表格某一行的数据
    :param cols_index: 获取sheet表格某一列或几列的数据
    :return: 返回字典或列表
    """
    xlUtils = XlrdUtils(xl_path)
    xl_dict = {}
    cell_list = []
    if sheet_index_or_name is not None and row_num is not None:
            cell_list.append(__get_cell_value(xlUtils, sheet_index_or_name, row_num, *cols_index))
    elif sheet_index_or_name is not None and row_num is None:
        for row_num in range(1, xlUtils.get_rows_num(sheet_index_or_name)):
            cell_list.append(__get_cell_value(xlUtils, sheet_index_or_name, row_num, *cols_index))
    elif sheet_index_or_name is None and row_num is not None:
        for sheet_index_or_name in range(0,len(xlUtils.get_sheet_names())):
            cell_list=[]
            cell_list.append(__get_cell_value(xlUtils, sheet_index_or_name, row_num, *cols_index))
            xl_dict[sheet_index_or_name] = cell_list
    elif sheet_index_or_name is None and row_num is None:
        for sheet_index_or_name in range(0,len(xlUtils.get_sheet_names())):
            cell_list = []
            for row_num in range(1,xlUtils.get_rows_num(sheet_index_or_name)):
                cell_list.append(__get_cell_value(xlUtils, sheet_index_or_name, row_num, *cols_index))
                if len(cell_list) != 0:
                    xl_dict[sheet_index_or_name] = cell_list
    if not xl_dict:
        if len(cell_list) != 0:
            xl_dict[sheet_index_or_name] = cell_list
    if sheet_index_or_name != None:
        return xl_dict[sheet_index_or_name]
    else:
        return xl_dict

def trans_data(dict_data:dict):
    payload = {}
    for K,V  in dict_data.items():
        if type(V) is dict:
            V = json.dumps(V, ensure_ascii=True)
        payload[K] = V
    return payload

def __get_cell_value(xlUtils:XlrdUtils, sheet_index_or_name, row_num,*cols_index):
    if len(cols_index)==0:
        case_num = xlUtils.get_cell_value(sheet_index_or_name, row_num, 0)
        moudle_name = xlUtils.get_cell_value(sheet_index_or_name, row_num, 1)
        case_name = xlUtils.get_cell_value(sheet_index_or_name, row_num, 2)
        request_method = xlUtils.get_cell_value(sheet_index_or_name, row_num, 3)
        request_url = xlUtils.get_cell_value(sheet_index_or_name, row_num, 4)
        request_headers = json.loads(xlUtils.get_cell_value(sheet_index_or_name, row_num, 5))
        params_desc = xlUtils.get_cell_value(sheet_index_or_name, row_num, 6)
        request_data = json.loads(xlUtils.get_cell_value(sheet_index_or_name, row_num, 7))
        except_result_desc = xlUtils.get_cell_value(sheet_index_or_name, row_num, 8)
        except_result = json.loads(xlUtils.get_cell_value(sheet_index_or_name, row_num, 9))
        return [case_num, moudle_name, case_name, request_method, request_url,
                trans_data(request_headers), params_desc, trans_data(request_data),
                except_result_desc, trans_data(except_result)]
    else:
        row_data = []
        for cell_cols_index in cols_index:
            row_data.append(xlUtils.get_cell_value(sheet_index_or_name, row_num, cell_cols_index))
        return row_data




class RD_By(object):
    CASE_NUM = 0
    MOUDLE_NAME = 1
    CASE_NAME = 2
    REQUEST_METHOD = 3
    REQUEST_URL = 4
    REQUEST_HEADERS = 5
    PARAMS_DESC = 6
    REQUEST_DATA = 7
    EXCEPT_RESULT_DESC = 8
    EXCEPET_RESULT = 9


#print(read_test_data("../../test_data/接口自动化用例设计.xls","登录",None, RD_By.REQUEST_DATA,RD_By.EXCEPET_RESULT))