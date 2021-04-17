# encoding = utf-8
"""
__title__ = ''
__author__ = 'davieyang'
__mtime__ = '2018/4/21'
"""
import time
import logging
from Configuration import ConstantConfig


class Logger:

    def __init__(self, logger):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        :param logger:
        """
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        logpath = "\\pubbookone\\TestResult\\TestLog\\"
        print(logpath)
        log_name = logpath + rq + '.log'
        filehandler = logging.FileHandler(log_name)
        filehandler.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        consolehandler = logging.StreamHandler()
        consolehandler.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        filehandler.setFormatter(formatter)
        consolehandler.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(filehandler)
        self.logger.addHandler(consolehandler)

    def getlog(self):
        return self.logger

