# -*- coding: UTF-8 -*-

import ConfigParser
import os


# 配置文件工具类
class ConfigUtils:
    def __init__(self):
        self.config = ConfigParser.ConfigParser()

    # 读取文件中的配置字段
    def read_config_para(self, config_file_name, param_name):
        if self.config is None:
            self.config = ConfigParser.ConfigParser()
        self.config.readfp(open(config_file_name))
        return self.config.get("ZIP", param_name)

    # 更新文件中的字段
    def update_config_para(self, config_file_name, param_name, param_value):
        if self.config is None:
            self.config = ConfigParser.ConfigParser()
        self.config.read(config_file_name)
        self.config.set("ZIP", param_name, param_value)
        self.config.write(open(config_file_name, "r+"))


# the main!
def main():
    if __name__ == "__main__":
        util = ConfigUtils()
        # 写配置文件
        config_file_name = "." + os.path.sep + "test" + os.path.sep + "test.ini"
        util.update_config_para(config_file_name, "A", "A value")
        util.update_config_para(config_file_name, "B", "B value")
        util.update_config_para(config_file_name, "C", "C value")
        # 读配置文件
        print util.read_config_para(config_file_name, "A")
        print util.read_config_para(config_file_name, "B")
        print util.read_config_para(config_file_name, "C")

# run！
main()
