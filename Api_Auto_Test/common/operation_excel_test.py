# -*- coding: utf-8 -*-

# @File: operation_excel
# @Author : "Sampson"
# @Detail :

import xlrd
import xlwt
from xlutils.copy import copy

from Api_Auto_Test import *
import platform


class Operation_Excel(object):

    __doc__ = "操作Excel表格"

    def __init__(self, filename=None, sheet_id=0):
        if filename:
            self.filename = filename
        else:
            self.filename = os.path.join(test_file_path, "auto_test_case.xlsx")
        self.sheet_id = sheet_id
        self.data = self.get_data()

    def get_data(self):
        """
        :return: tables object 返回一个sheet操作对象
        """
        data = xlrd.open_workbook(self.filename)
        return data.sheets()[self.sheet_id]


    def get_lines(self):
        """
        获取单元格行数
        :return:
        """
        return self.data.nrows

    def get_cell_value(self, row, col):
        """
        获取某个单元格的内容
        :param row: 行
        :param col: 列
        :return:
        """
        return self.data.cell_value(row, col)

    def write_value(self, row, col, value):
        read_data = xlrd.open_workbook(self.filename, formatting_info=True)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.filename)

    # 根据case_id找到对应行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_value(row_num)
        return rows_data

    # 根据对应的case_id 找到对应行的行号
    def get_row_num(self, case_id):
        num = 0
        cols_data = self.get_cols_data()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num += 1

    # 根据行号，找到该行的内容
    def get_row_value(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # 获取某一列的内容
    def get_cols_data(self, col_id=None):
        if col_id:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols

if __name__ == '__main__':
    opens = Operation_Excel()
    print(opens.get_lines())
    print(opens.get_cell_value(0,2))
