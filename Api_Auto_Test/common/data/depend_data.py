# -*- coding: utf-8 -*-

# @File: depend_data
# @Author : "Sampson"
# @Detail : 处理数据依赖问题
# @time : 

from Api_Auto_Test.common.operation_excel_test import Operation_Excel
from Api_Auto_Test.common.runMethod import RunMethod
from Api_Auto_Test.common.data.get_data_excel import Get_Data
from jsonpath_rw import jsonpath,parse
import json

class depend_Data:
    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = Operation_Excel()
        self.data = Get_Data()

    """ 通过case-id去获取case_id的整行数据"""
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    def run_depend(self):
        run_method = RunMethod()
        row_num = self.opera_excel.get_row_num(self.case_id)
        host = self.data.get_Host(row_num)
        url = host + self.data.get_request_url(row_num)
        request_data = self.data.get_request_data(row_num)
        header = self.data.get_header(row_num)
        method = self.data.get_request_method(row_num)

        res = run_method.run_main(method, url, request_data, header)
        return json.loads(res)

    def get_data_for_case_depend_key(self, row):
        """ 根据依赖的 key 去获取执行依赖测试 case 的响应，然后返回 """
        depend_data = self.data.get_data_depend(row)
        response_data = self.run_depend()
        json_exe = parse(depend_data)
        result = json_exe.find(response_data)
        ret_list = [match.value for match in result]
        if ret_list:
            return ret_list[0]
        else:
            return None


if __name__ == '__main__':
    dep = depend_Data("myIndex-4")
    res = dep.get_data_for_case_depend_key(5)
    print(res)
