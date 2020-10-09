# -*- coding:utf-8 -*-
"""
@project : CCMS
@author:hyongchang
@file:conftest.py
@ide: PyCharm
@time: 2020-10-08 17:49
"""
import sys
import os,subprocess
import pytest, allure

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

@pytest.fixture(scope="session", autouse=True)
def init_env_info():
    # 置前操作
    with allure.step("删除allure报告"):
        print("删除allure报告")
        os.system(r"rd /s /q ..\report\allure\tmp")
        os.system(r"rd /s /q ..\report\allure\allure_report")
    with allure.step("删除测试覆盖率测试报告"):
        print("删除测试覆盖率测试报告")
        os.system(r"rd /s /q ..\report\htmlcov")
    with allure.step("创建allure测试报告tmp文件目录"):
        os.system(r"mkdir ..\report\allure\tmp")
        os.system(r"mkdir ..\report\allure\allure_report")

    yield
    # 置后操作
    with allure.step("环境配置文件信息"):
        lib_versions = {
            "python": "python -V",
            "Browser": "Chrome 138"
        }
        f = open(f"{sys.path[0]}/report/allure/tmp/environment.properties", "a+")
        with allure.step("获取相关库的版本信息"):
            lib_versions_list = ["pytest","selenium","xlrd","requests"]
            for lib_version_one in lib_versions_list:
                result = os.popen(f"pip3 list|findstr {lib_version_one}").read()
                for line in result.split("\n"):
                    if line:
                        lib_info = line.split(" ")
                        lib_str = lib_info[0]
                        lib_version = lib_info[-1]
                        f.write(f"{lib_str}={lib_version}\n")

        for K, V in lib_versions.items():
            try:
                stdout, stderr = subprocess.Popen(V, stdout=subprocess.PIPE).communicate()
                result = stdout.decode("gbk")
                f.write(f"{K}={result}")
            except EnvironmentError:
                f.write(f"{K}={V}")
        f.close()

