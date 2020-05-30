# -*- coding: utf-8 -*-

# @File: 操作json文件
# @Author : "Sampson"
# @Detail :

import json
from Api_Auto_Test import json_path


class Operation_Json(object):

    __doc__ = "操作JSON"

    def __init__(self, filename=None):
        if filename:
            self.filename = json_path + "/" + filename + ".json"
        else:
            self.filename = json_path + "/myPage.json"
        self.data = self.read_data()

    def read_data(self):
        with open(self.filename) as fp:
            data = json.load(fp)
        return data

    def get_data(self, keys):
        key_lists = keys.split(".")
        data = self.data
        for i in key_lists:
            data = data[i]
        return data

if __name__ == '__main__':
    op = Operation_Json()
    print(op.get_data("addCar"))