# -*- coding:utf-8 -*-
"""
@project : CCMS
@author:hyongchang
@file:DateUtils.py
@ide: PyCharm
@time: 2020-09-30 22:10
"""
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from datetime import datetime,timedelta

class DateUtils():
    """
    时间公共类
    """

    @staticmethod
    def get_current_hour(split="-",days=0,hours=0,minutes=0):
        """
        获取当前时间：格式YYYY-MM-DD hh:mm
        :param split:日期格式分隔符
        :param days: 当前日期加减天数
        :param hours:当前日期加减小时数
        :param minutes:当前日期加减分钟数
        :return:返回当前时间
        """
        return (datetime.now()+timedelta(days=days)+
                timedelta(hours=hours)+timedelta(minutes=minutes)
                ).strftime(f"%Y{split}%m{split}%d %H:%M")


    @staticmethod
    def get_current_time(split="-",days=0,hours=0,minutes=0):
        """
        获取当前时间：格式YYYY-MM-DD hh:mm:ss
        :param split:日期格式分隔符
        :param days: 当前日期加减天数
        :param hours:当前日期加减小时数
        :param minutes:当前日期加减分钟数
        :return:返回当前时间
        """
        return (datetime.now()+timedelta(days=days)+
                timedelta(hours=hours)+timedelta(minutes=minutes)).strftime(f"%Y{split}%m{split}%d %X")

    @staticmethod
    def get_current_date(split="-",days=0):
        """
        获取当前时间：格式YYYY-MM-DD
        :param split:日期格式分隔符
        :param days: 当前日期加减天数
        :return:返回当前日期
        """
        return (datetime.now()+timedelta(days=days)).strftime(f"%Y{split}%m{split}%d")
