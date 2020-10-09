# -*- coding: UTF-8 -*-

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import pytest
"""
测试文件以test开头或结尾
测试类以Test开头，T必须大写，不能带有init方法
测试函数以test开头或结尾
断言使用基本的assert即可
"""


def execute_case():
    # 运行整个测试文件目录
    pytest.main(["-s", "../test_case", "--reruns=2", "--reruns-delay=1",
                 "--html=../report/allure/user.html",
                 "--junitxml=../report/allure/user.xml",
                 "--alluredir", "../report/allure/tmp/",
                 "-vv", "--cov=..\\test_case", "--cov-report=html"])  # 测试代码覆盖率
    os.system("allure generate ../report/allure/tmp -o ../report/allure/allure_report --clean")
    os.system(f"move htmlcov {rootPath}\\report")


if __name__ == "__main__":
    execute_case()









