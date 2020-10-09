# -*- coding:utf-8 -*-
"""
@project : CCMS
@author:hyongchang
@file:test_schedule.py
@ide: PyCharm
@time: 2020-10-08 17:51
"""
import sys
import os
import pytest,allure
from utils.CommonUtils.DateUtils import DateUtils
from utils.CommonUtils.AllureUtils import AllureUtils
from config.config import admin_email,admin_password,email,password
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


@allure.feature("日程功能测试")
class TestSchedule:

    @pytest.fixture()
    def before_auto_ui(self,init_browser):
        login = init_browser
        main_page = login.login(admin_email,admin_password)
        yield main_page
        main_page.logout()


    @AllureUtils.dynamic_story("topic_name")
    @pytest.mark.parametrize("topic_name,address,desc",[("中秋佳节","会议室A01","全员参与，勿迟到!!"),
                                                        ("国庆快乐","会议室A03","全员参与，勿迟到!!")])
    def test_tc005001(self,topic_name,address,desc,before_auto_ui):
        self.main_page = before_auto_ui
        assert self.main_page.to_schedule().new_schedule(topic_name=topic_name,
                                                         address=address,desc=desc).\
            logout().login(email,password).check_schedule(topic_name) == True

    @AllureUtils.dynamic_story("topic_name")
    @pytest.mark.parametrize("topic_name,address,desc", [("中秋佳节!!!", "会议室B01", "全员参与，勿迟到!!"),
                                                         ("国庆快乐!!!", "会议室B03", "全员参与，勿迟到!!")])
    def test_tc005002(self,topic_name,address,desc,before_auto_ui):
        self.main_page = before_auto_ui
        assert self.main_page.to_schedule().\
            new_schedule(topic_name=topic_name,start_date=DateUtils.get_current_hour(days=2),
                         end_date=DateUtils.get_current_hour(days=3),
                         address=address,desc=desc).logout().login(email, password).\
            check_schedule(topic_name) == False

