# -*- coding: utf-8 -*-
import logging
from common.settings import get_log_path
import datetime
import os

class Logger:
    def __init__(self, log_file):
        self.logger = logging.getLogger('logger')
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        file_handler = logging.FileHandler(log_file, encoding='utf8')
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)
    
    def exception(self, message):
        self.logger.exception(message)

# todo 每天生成一个log文件

log_filename = datetime.datetime.now().strftime("%Y-%m-%d.log")

log_path = os.path.join(get_log_path(), log_filename)
logger = Logger(log_path)

if __name__ == "__main__":
    logger = logger(get_log_path() + "test.log")
    logger.info("This is an info message.")
    logger.error("This is an error message.")
