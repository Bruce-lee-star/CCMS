# -*- coding:utf-8 -*-
"""
@author:hyongchang
@file:test_case_07.py
@time:2020/07/01
"""
from configparser import ConfigParser
import os

class ConfigFileUtils:

    def __init__(self, config_file, encode="utf-8"):
        if os.path.exists(config_file):
            self.__cfg_file = config_file
        else:
            raise FileNotFoundError()
        self.__config = ConfigParser()
        self.__config.read(config_file, encoding=encode)

    def get_sections(self):
        return self.__config.sections()

    def get_options(self,section_name):
        if self.__config.has_section(section_name):
            return self.__config.options(section_name)
        else:
            raise ValueError(section_name)

    def get_option_value(self, section_name, option_name):
        if self.__config.has_option(section_name, option_name):
            return self.__config.get(section_name, option_name)
        else:
            raise ValueError(section_name, option_name)

    def get_all_items(self, section):
        if self.__config.has_section(section):
            return self.__config.items(section)

    def print_all_items(self):
        for section in self.get_sections():
            print("[" + section + "]")
            for K, V in self.__config.items(section):
                print(K + "=" + V)

    def add_new_section(self, new_section):
        if not self.__config.has_section(new_section):
            self.__config.add_section(new_section)
            self.__update_cfg_file()

    def add_option(self, section_name, option_key, option_value):
        if self.__config.has_section(section_name):
            self.__config.set(section_name, option_key, option_value)
            self.__update_cfg_file()

    def del_section(self, section_name):
        if self.__config.has_section(section_name):
            self.__config.remove_section(section_name)
            self.__update_cfg_file()

    def del_option(self, section_name, option_name):
        if self.__config.has_option(section_name, option_name):
            self.__config.remove_option(section_name, option_name)
            self.__update_cfg_file()

    def update_option_value(self,section_name, option_key, option_value):
        if self.__config.has_option(section_name,option_key):
            self.add_option(section_name, option_key, option_value)

    def __update_cfg_file(self):
        with open(self.__cfg_file, "w") as f:
            self.__config.write(f)
