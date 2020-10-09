# -*- coding:utf-8 -*-
"""
@author:hyongchang
@file:test_case_07.py
@time:2020/07/01
"""
import xlrd

class XlrdUtils(object):

    def __init__(self,filename):
        self.workbook = xlrd.open_workbook(filename, formatting_info=True)

    def get_cell_value(self, sheet_index_or_name, row_index, col_index):
        sheet = self.__get_sheet(sheet_index_or_name)
        if sheet.nrows and sheet.ncols:
            return sheet.cell_value(row_index, col_index)
        else:
            raise BaseException("Index out of range!")

    def __get_sheet(self, sheet_index_or_name):
        """
        根据sheet的索引或名称，获取sheet对象
        :param sheet_index_or_name: sheet的索引或名称
        :return:sheet对象
        """
        if isinstance(sheet_index_or_name, int):
            if len(self.workbook.sheet_names()) > sheet_index_or_name:
                return self.workbook.sheet_by_index(sheet_index_or_name)
            else:
                raise BaseException("Invalid Sheet Index!")
        elif isinstance(sheet_index_or_name, str):
            if sheet_index_or_name in self.workbook.sheet_names():
                return self.workbook.sheet_by_name(sheet_index_or_name)
            else:
                raise BaseException("Invalid Sheet Name!")
    def get_rows_num(self,sheet_index_or_name):
        return self.__get_sheet(sheet_index_or_name).nrows

    def get_cols_num(self,sheet_index_or_name):
        return self.__get_sheet(sheet_index_or_name).ncols

    def get_sheet_names(self):
        return self.workbook.sheet_names()

    def items_value(self, sheet_index_or_name):
        """
        打印sheet页的表格数据
        :param sheet_index_or_name:sheet的索引或名称
        :return:
        """
        sheet = self.__get_sheet(sheet_index_or_name)
        for row in range(0, sheet.nrows):
            for col in range(0, sheet.ncols):
                print(self.get_cell_value(sheet_index_or_name, row, col), end="\t")
            print()

    @staticmethod
    def datatodict(data):
        """
        从表格获取单元格的数据转化为字典
        :return:
        """
        str_data = data.replace("{", "").replace("}", "")
        data_split = str_data.split(",")
        dict_data = {}
        for dat in data_split:
            k, v = dat.split(':')
            dict_data[k] = v
        return dict_data
