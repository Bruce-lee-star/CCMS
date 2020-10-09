# -*- coding: UTF-8 -*-

import sys
import os
from service.webui.BasePage import BasePage
from config.config import HOST

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


class LoginPage(BasePage):

    def __init__(self):
        super().__init__()
        self.to_page(HOST)

    # 登录操作
    def login(self, email, password):
        self.input(self.email_input, email)
        self.input(self.password_input, password)
        self.click(self.login_btn)
        return MainPage()


class MainPage(BasePage):

    # 日程
    def to_schedule(self):
        self.click(self.daily_schedule_a)
        return SchedulePage()

    # 点击主页头像
    def click_person_img(self):
        self.click(self.person_img)
        return self

    # 注销操作
    def logout(self):
        self.click_person_img()
        self.click(self.exit_a)
        return LoginPage()

    # 获取登录用户名
    def get_username(self):
        return self.click_person_img().get_text(self.username_span)

    # 检查日程信息
    def check_schedule(self, schedule_text):
        return schedule_text in self.get_group_text(self.schedule_list_a)


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



