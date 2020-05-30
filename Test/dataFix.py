# -*- coding: utf-8 -*-

# @File: functions
# @Author : "Sampson"
# @Detail :


import os
import re
import xlrd
import xlwt
from xlutils.copy import copy


class ScoreFix:
    def __init__(self):
        self.dirPath = os.path.abspath(os.path.dirname(__file__))

    def open_data_fix(self):
        path = os.path.join(self.dirPath, "dataFix.sql")
        readers = open(path, "r")
        return readers


def write_excel_xls_append(path, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            new_worksheet.write(i+rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save(path)  # 保存工作簿
    print("xls格式表格【追加】写入数据成功！")


if __name__ == '__main__':
    scoreFix = ScoreFix()
    readers = scoreFix.open_data_fix()

    regMember_cup = re.compile(r"= (.+?),")
    regMain_id = re.compile(r"(\d+)+;")
    values = []

    for reader in readers:
        value = []
        member_cup = re.findall(regMember_cup, reader)
        main_id = re.findall(regMain_id, reader)
        value.append(member_cup[0])
        value.append("M" + main_id[0])
        values.append(value)

    path = "/Users/deyoukong/Desktop/dataFixs.xls"
    write_excel_xls_append(path=path, value=values)

