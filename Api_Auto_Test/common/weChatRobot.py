# -*- coding: utf-8 -*-

__author__ = "Sampson"

import requests
import json

def send_msg():
    global data
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=4d463aaf-e707-4212-a560-2e1a4d56b9ce"
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "news",
        "news": {
            "articles": [
                {
                    "title": "测试汇报",
                    "description": "测试消息测试消息",
                    "url": "URL",
                    "picurl": "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png"
                }
            ]
        }
    }

    rsp = requests.post(url=url, data=json.dumps(data), headers=headers)
    rsp_json = rsp.json()
    print(rsp_json)