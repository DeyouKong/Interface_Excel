# -*- coding: utf-8 -*-

# @File: get_data
# @Author : "Sampson"
# @Detail :


from Api_Auto_Test.common.operation_excel_test import Operation_Excel
from Api_Auto_Test.common.data import data_config_excel
from Api_Auto_Test.common.operation_json import Operation_Json
import json
import xlrd

class Get_Data:
    def __init__(self, filename=None, sheet_id=0):
        self.operation_excel = Operation_Excel(filename, sheet_id)

    def get_excel_lines(self):
        """ 获取文件总行数 """
        return self.operation_excel.get_lines()

    def get_is_run(self, row):
        """ 获取是否执行 """
        flag = True
        col = data_config_excel.get_IS_RUn_col()
        run_model = self.operation_excel.get_cell_value(row, col)
        if run_model not in ("yes", "1"):
            flag = False
        return flag

    def get_Host(self, row):
        """ 获取地址 """
        col = data_config_excel.get_Host_col()
        return self.operation_excel.get_cell_value(row, col)

    def get_request_url(self, row):
        """ 获取请求地址 """
        col = data_config_excel.get_Request_Url_col()
        url = self.operation_excel.get_cell_value(row, col)
        return url

    def get_request_method(self, row):
        """ 获取请求方法 """
        col = data_config_excel.get_Method_col()
        request_method = self.operation_excel.get_cell_value(row, col)
        return request_method

    def get_header(self, row):
        """ 获取请求头 """
        col = data_config_excel.get_Is_Header_col()
        is_header = self.operation_excel.get_cell_value(row, col)
        header_data = None
        if is_header in ("yes", "1"):
            col = data_config_excel.get_Header_Value_col()
            header = self.operation_excel.get_cell_value(row, col)
            op_json = Operation_Json("header")
            header_data = op_json.get_data(header)
            if "Authorization" in header_data.keys():
                Authorization_col = data_config_excel.get_Authorization_col()
                Authorization = self.operation_excel.get_cell_value(1, Authorization_col)
                header_data["Authorization"] = Authorization
            return header_data
        return header_data


    def get_request_data(self, row):
        """ 获取请求数据 """
        col = data_config_excel.get_Request_Data_col()
        data = self.operation_excel.get_cell_value(row, col)
        if data:
            op_json = Operation_Json()
            return op_json.get_data(data)
        else:
            return None

    def get_except_data(self, row):
        """ 获取预期结果值 """
        col = data_config_excel.get_Expect_col()
        return self.operation_excel.get_cell_value(row, col)

    def get_case_depend(self, row):
        """ 获取用例依赖 """
        col = data_config_excel.get_Case_Depend_col()
        return self.operation_excel.get_cell_value(row, col)

    def get_data_depend(self, row):
        """ 获取依赖数据的 key """
        col = data_config_excel.get_Data_Depend_col()
        return self.operation_excel.get_cell_value(row, col)

    def get_field_depend(self, row):
        """ 获取依赖舒服的字段 """
        col = data_config_excel.get_Field_Depend_col()
        return self.operation_excel.get_cell_value(row, col)

    def write_result(self, row, value=None, res=None, Authorization=None):
        result_col = int(data_config_excel.get_Result_col())
        response_col = int(data_config_excel.get_Response_data_col())
        Authorization_col = int(data_config_excel.get_Authorization_col())
        if res:
            self.operation_excel.write_value(row, result_col, value)
            self.operation_excel.write_value(row, response_col, res)
        else:
            self.operation_excel.write_value(row, result_col, value)
            self.operation_excel.write_value(row, response_col, "")
        if Authorization:
            self.operation_excel.write_value(1, Authorization_col, Authorization)


if __name__ == '__main__':
    data = Get_Data()
    header = data.get_header(1)
    print(type(header), header)

    request = data.get_request_data(1)
    print(type(request), request)
