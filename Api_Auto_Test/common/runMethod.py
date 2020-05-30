# -*- coding: utf-8 -*-

# @File: runMethod
# @Author : "Sampson"
# @Detail :
# @time : 

import requests
import json

class RunMethod:

    def post_main(self, url, data=None, header=None):
        res = None
        if header:
            res = requests.post(url=url, json=data,headers=header)
        else:
            res = requests.post(url=url, data=data)

        return res

    def get_main(self, url, data=None, header=None):
        res = None
        if header:
            if data:
                res = requests.get(url=url, params=data, headers=header)
            else:
                res  = requests.get(url=url, headers=header)
        else:
            res = requests.get(url=url, params=data)
        return res

    def run_main(self, method, url, data=None, header=None):
        """
        执行接口主入口，返回一个json格式的字符串 <str>
        :param method: 请求方法
        :param url: 请求url
        :param data: 请求数据
        :param header: 请求头
        :return:
        """
        res = None
        if method == "post":
            res = self.post_main(url, data, header)
        elif method == "get":
            res = self.get_main(url, data, header)

        res = res.json()
        return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)

