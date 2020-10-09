# -*- coding:utf-8 -*-
"""
@project : CCMS
@author:hyongchang
@file:SchedulePage22.py
@ide: PyCharm
@time: 2020-10-08 8:32
"""
import sys
import os
from service.webui.MainPage11 import MainPage
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

class SchedulePage(MainPage):

    # 新建日程
    def new_schedule(self,topic_name,start_date=None,end_date=None,is_all_day=False,address=None,desc=None):
        # 新建按钮
        self.click(self.new_btn)
        self.input(self.topic_name_input,topic_name)
        # 日期控件的选择
        if start_date:
            self.date_ctrl(self.start_date_input,start_date)
        if end_date:
            self.date_ctrl(self.end_date_input, end_date)
        # 分派任务
        self.click(self.users_selected)
        self.click_group(self.users_deselected)
        self.click(self.target_select_user)
        self.click(self.confirm_btn)
        if is_all_day:
            self.click(self.all_day_checkbox)
        if address:
            self.input(self.address_input,address)
        if desc:
            self.input(self.desc_area,desc)
        self.click(self.save_btn)
        return self




if __name__ == '__main__':
    from config.config import admin_email, admin_password
    from service.webui.Business import LoginPage
    from service.webui.MainPage11 import MainPage
    LoginPage().login(admin_email, admin_password)
    MainPage().to_schedule().new_schedule("111111").logout()


