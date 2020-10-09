# -*- coding:utf-8 -*-
"""
@author:hyongchang
@file:config.py
@time:2020/07/11
"""
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from utils.CommonUtils.ConfigParserUtils import ConfigFileUtils
from utils.ApiUtils.PyMysqlUtils import PyMySQLUtils

# 各环境主机配置
test_host = "https://xxxxxx"
dev_host = "http://xxxxxx"
HOST = "http://devops.sqtest.online:6003"

# 登录管理员信息
admin_email = "1668464993@qq.com"
admin_password = "123456"
admin_login_payload = {"user":{"email": f"{admin_email}"}, "password": f"{admin_password}", "code": "", "locale": "zh-cn"}

# 登录普通用户信息
email = "1668464993@163.com"
password = "123456"
login_payload = {"user":{"email": f"{email}"}, "password": f"{password}", "code": "", "locale": "zh-cn"}


# 定位元素显示等待配置信息
TIME_OUT = 20
POLL_FREQUENCY = 0.5

# 获取数据库连接对象
def get_sql_utils():
    config = ConfigFileUtils("../config/api.cfg")
    host = str(config.get_option_value("run_database_cfg", "host"))
    user = str(config.get_option_value("run_database_cfg", "user"))
    password = str(config.get_option_value("run_database_cfg", "password"))
    database = str(config.get_option_value("run_database_cfg", "database"))
    port = int(config.get_option_value("run_database_cfg", "port"))
    charset = str(config.get_option_value("run_database_cfg", "charset"))
    return PyMySQLUtils(host=host, user=user, password=password,
                        database=database, port=port, charset=charset)

