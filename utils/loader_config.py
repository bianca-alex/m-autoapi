# coding=utf-8
from configparser import ConfigParser
from common.settings import get_config_path
from utils.logger import logger
import os


class Config:
    def __init__(self, filename=None):
        self.config = ConfigParser()
        if filename == None:
            config_path = os.path.join(get_config_path(), "setting.ini")
            self.config.read(config_path, encoding='utf8')
        else:
            config_path = os.path.join(get_config_path(), filename + ".ini")
            self.config.read(config_path, encoding='utf8')


    def get(self, key, node=None):
        if node == None:
            node = 'Test'
        cf = self.config
        try:
            data = cf.get(node, key)
            logger.info('获取配置文件的值，node：{},key：{}, data：{}'.format(node, key, data))
        except Exception:
            logger.exception('没有获取到对应的值，node：{},key：{}'.format(node, key))
            data = None
        return data


config = Config()

if __name__ == "__main__":
    print(config.get("key"))
