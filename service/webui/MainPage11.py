# -*- coding: UTF-8 -*-

import sys
import os
from service.webui.BasePage import BasePage
from service.webui.SchedulePage22 import SchedulePage
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


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

