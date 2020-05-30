# -*- coding: utf-8 -*-

# @File: Case_baidu
# @Author : "Sampson"
# @Detail :

from Api_Auto_Test import *
import json

class Weather(unittest.TestCase):

    def setUp(self):
        self.log = log
        self.url = "http://www.weather.com.cn/data/cityinfo/101010100.html"

    def tearDown(self):
        pass

    def test_getWeather(self):
        log.info("请求获取天气url：%s" % self.url)
        resp = requests.get(url=self.url)
        print(resp)

