#-*- coding: UTF-8 -*-

import sys
import os
import time

from selenium import webdriver
from utils.CommonUtils.YamlUtils import YamlUtils
from config.config import TIME_OUT, POLL_FREQUENCY
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


class WebDriverUtils:
    # 类属性
    __browser_type = None  # 浏览器类型
    # 浏览器类型
    Firefox = "Firefox"
    Chrome = "Chrome"
    ie = "Ie"
    Edge = "Edge"
    Opera = "Opera"
    Safari = "Safari"

    # 单例设计模式
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance = object.__new__(cls)
        return cls._instance

    # 单例设计模式
    @classmethod
    def get_driver(cls, browser_type="Chrome"):
        if not hasattr(cls, "driver"):
            if browser_type == "Firefox":
                cls.driver = webdriver.Firefox()
            elif browser_type == "Ie":
                cls.driver = webdriver.Ie()
            elif browser_type == "Edge":
                cls.driver = webdriver.Edge()
            elif browser_type == "Opera":
                cls.driver = webdriver.Opera()
            elif browser_type == "Safari":
                cls.driver = webdriver.Safari()
            else:
                cls.driver = webdriver.Chrome()
        return cls.driver


class BasePage:

    def __init__(self):
        self.__driver = WebDriverUtils.get_driver(WebDriverUtils.Chrome)
        self.__driver.maximize_window()
        self.__driver.set_page_load_timeout(60) # 设置页面加载超时
        self.__driver.set_script_timeout(10) # 设置页面异步js执行超时
        # 动态获取元素定位
        self.dynamic_bind_ele_locator()

    def dynamic_bind_ele_locator(self):
        """
        实现动态绑定继承树相关类元素定位的加载
        :return:
        """
        classes_name = self.__class__.mro()[:-2] # 获取继承树，排除BasePage和Object类
        for class_name in classes_name:
            elements_locator_info = YamlUtils.read_yml(f"{curPath}/../../config/web_locator.yml")[class_name.__name__]
            for element_locator, element_value in elements_locator_info.items():
                self.__setattr__(element_locator, element_value)

    # 定位单个元素
    def get_element(self, locator):
        WebDriverWait(
            # 传入浏览器对象
            driver=self.__driver,
            # 传入超时时间
            timeout=TIME_OUT,
            # 设置轮询时间
            poll_frequency=POLL_FREQUENCY).until(
            # 检查元素是否可见
            EC.visibility_of_element_located(locator)
        )

        # 返回元素对象，元组传参
        return self.__driver.find_element(*locator)

    # 定位一组元素
    def get_elements(self, locator):
        WebDriverWait(driver=self.__driver,
                      timeout=TIME_OUT,
                      poll_frequency=POLL_FREQUENCY
                      ).until(
            EC.visibility_of_all_elements_located(locator)
        )
        return self.__driver.find_elements(*locator)

    # 跳转至指定路径
    def to_page(self, url):
        self.__driver.get(url)

    # 文本框输入指定内容
    def input(self, locator, value):
        self.get_element(locator).send_keys(value)

    # 鼠标左击操作
    def click(self, locator):
        self.get_element(locator).click()

    # 点击一组元素的每一个元素
    def click_group(self,locator):
        time.sleep(1)
        for ele in self.get_elements(locator):
            ele.click()

    # 获取title
    def get_title(self):
        return self.__driver.title

    # 获取元素文本内容
    def get_text(self,locator):
        return self.get_element(locator).text

    # 获取一组元素的文本内容
    def get_group_text(self,locator):
        return [ele.text for ele in self.get_elements(locator)]

    # 执行js脚本
    def execute_js(self,script):
        self.__driver.execute_script(script)

    # 日期控件
    def date_ctrl(self,locator,date_value):
        time.sleep(1)
        self.execute_js(f"document.querySelector(\"{locator[1]}\").value=\'{date_value}\'")

    def close_browser(self):
        self.__driver.quit()

