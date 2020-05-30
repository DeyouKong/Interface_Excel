# -*- coding: utf-8 -*-

# @File: Api_Auto_Test.__init__.py
# @Author : "Sampson"
# @Detail :

import sys
from Api_Auto_Test.common.HTMLReport import BeautifulReport
from Api_Auto_Test.common import logger
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64
from datetime import datetime
import configparser
import requests
import pymysql
import time
import json
import platform
import os
import unittest

base_dir = os.path.abspath(os.path.dirname(__file__))

# 初始化配置文件路径
conf_path = "/config/mainConfig" if platform.system() != "Windows" else '\config\mainConfig'
conf_file_path = base_dir + conf_path
conf = configparser.RawConfigParser()
conf.read(filenames=conf_file_path, encoding="utf-8")

# 初始化logger
logger.__DEBUG__ = True
log = logger.Log(os.path.basename(__file__)).logger_file()

json_path = base_dir + '/TestFiles/JsonData' if platform.system() != 'Windows' else '\TestFiles\TJsonData'


test_file_path = base_dir + '/TestFiles/TestData' if platform.system() != 'Windows' else '\TestFiles\TestData'

report_path = base_dir + '/TestFiles/TestReport' if platform.system() != 'Windows' else '\TestFiles\TestReport'


