# -*- coding: utf-8 -*-

__author__ = "Sampson"

import logging
import os
import colorlog
from _datetime import datetime
import platform


# pro_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# file_name = os.path.join(pro_path, 'logs')
# class Log():
#     def __init__(self):
#         self.logname = os.path.join(file_name,'%s.log'%time.strftime('%Y-%m-%d'))
#         self.logger = logging.getLogger()
#         self.logger.setLevel(logging.DEBUG)
#         self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:[line:%(lineno)d]:%(message)s')
#
#     def console(self,level,message):
#         fh = logging.FileHandler(self.logname,'a',encoding='utf-8')
#         fh.setLevel(logging.DEBUG)
#         fh.setFormatter(self.formatter)
#         self.logger.addHandler(fh)
#         ch = logging.StreamHandler()
#         ch.setLevel(logging.DEBUG)
#         ch.setFormatter(self.formatter)
#         self.logger.addHandler(ch)
#         if level == 'info':
#             self.logger.info(message)
#         elif level == 'debug':
#             self.logger.debug(message)
#         elif level == 'warning':
#             self.logger.warning(message)
#         elif level == 'error':
#             self.logger.error(message)
#
#         self.logger.removeHandler(ch)
#         self.logger.removeHandler(fh)
#         fh.close()
#
#     def debug(self,message):
#         self.console('debug',message)
#
#     def info(self,message):
#         self.console('info',message)
#
#     def warning(self,message):
#         self.console('warning',message)
#
#     def error(self,message):
#         self.console('error',message)



curPath = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
logPath = curPath + "/logs/" if platform.system() != "Windows" else  curPath + "\logs\\"

if not os.path.exists(logPath):
    os.makedirs(logPath)

log_name = logPath + datetime.strftime(datetime.now(), '%Y-%m-%d') + ".log"

log_colors_config = {
    "DEBUG": "yellow",
    "INFO": "cyan",
    "WARNING": "green",
    "ERROR": "red",
    "CRITICAL": "red",
}

__DEBUG__ = True

class Log(object):

    __doc__ = "控制台写入和日志文件写入分离"

    def  __init__(self, logger_name):
        self.fh = logging.FileHandler(filename=log_name, mode="a", encoding="utf-8")
        self.sh = logging.StreamHandler()
        self.logger_fh = logging.getLogger("logger_file")
        self.logger_sh = logging.getLogger(logger_name)

        if __DEBUG__:
            self._SET_LEVEL = logging.DEBUG
        else:
            self._SET_LEVEL = logging.INFO
        self.formatters = colorlog.ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(filename)s:[line:%(lineno)d] : %(message)s', "%Y-%m-%d %H:%M:%S", log_colors=log_colors_config)
        self.formatter = logging.Formatter('%(asctime)s -  %(levelname)s - %(filename)s:[line:%(lineno)d] : %(message)s', "%Y-%m-%d %H:%M:%S")

    def close_logger(self):
        """
        关闭 logger ，一般不用
        :return:
        """
        self.logger_fh.removeFilter(self.fh)
        self.logger_sh.removeFilter(self.sh)
        self.sh.close()
        self.fh.close()

    def logger_stream(self):
        """
        :return: logger object，返回一个控制台日志的 logger
        """
        self.logger_sh.setLevel(self._SET_LEVEL)
        self.sh.setFormatter(self.formatters)
        self.logger_sh.addHandler(self.sh)
        self.logger_sh.propagate = False
        return self.logger_sh

    def logger_file(self):
        """
        :return: logger object ，返回一个写日志文件的 logger
        """
        self.logger_fh.setLevel(self._SET_LEVEL)
        self.fh.setFormatter(self.formatter)
        self.logger_fh.addHandler(self.fh)
        self.logger_fh.propagate = False
        return self.logger_fh


class Logger(object):

    __doc__ = "控制台和日志同时写入"

    def __init__(self, name):
        self.fh = logging.FileHandler(filename=log_name, mode='a', encoding='utf-8')
        self.sh = logging.StreamHandler()
        self.logger = logging.getLogger(name=name)
        if __DEBUG__:
            self._SET_LEVEL = logging.DEBUG
        else:
            self._SET_LEVEL = logging.INFO
        self.formatters = colorlog.ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(filename)s:[line:%(lineno)d] | %(message)s', "%Y-%m-%d %H:%M:%S", log_colors=log_colors_config)
        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:[line:%(lineno)d] | %(message)s', "%Y-%m-%d %H:%M:%S")
        self.sh.setFormatter(self.formatters)
        self.fh.setFormatter(self.formatter)
        self.logger.setLevel(self._SET_LEVEL)
        self.logger.addHandler(self.sh)
        self.logger.addHandler(self.fh)
        self.logger.propagate = False

    def close_logger(self):
        self.logger.removeHandler(self.sh)
        self.logger.removeHandler(self.fh)
        self.fh.close()
        self.sh.close()

    def log(self):
        return self.logger

if __name__ == "__main__":
    __DEBUG__ = True
    log = Log(os.path.basename(__file__)).logger_file()
    log.debug("debug日志")
    log.info("info日志")
    log.warning("warning日志")
    log.error("error日志")
    log.critical("critical日志")