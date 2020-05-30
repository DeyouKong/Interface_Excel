# -*- coding: utf-8 -*-

# @File: 获取常量
# @Author : "Sampson"
# @Detail :


class global_var:
    API_Id = 0
    API_Name = 1
    Host = 2
    Request_Url = 3
    Method = 4
    is_Header = 5
    Header_value = 6
    Case_Depend = 7
    Data_Depend = 8
    Field_Depend = 9
    Request_Data = 10
    Expect = 11
    Result = 12
    Response_data = 13
    Is_Run = 14
    Authorization = 15


def get_API_Id_col():
    """获取API的ID"""
    return global_var.API_Id


def get_API_Name_col():
    """
    获取API的name
    :return:
    """
    return global_var.API_Name

def get_Host_col():
    """
    获取API的name
    :return:
    """
    return global_var.Host

def get_Request_Url_col():
    """

    :return:
    """
    return global_var.Request_Url

def get_Method_col():
    """

    :return:
    """
    return global_var.Method

def get_Is_Header_col():
    """

    :return:
    """
    return global_var.is_Header

def get_Header_Value_col():
    """

    :return:
    """
    return global_var.Header_value


def get_Case_Depend_col():
    """

    :return:
    """
    return global_var.Case_Depend

def get_Data_Depend_col():
    """

    :return:
    """
    return global_var.Data_Depend

def get_Field_Depend_col():
    """

    :return:
    """
    return global_var.Field_Depend


def get_Request_Data_col():
    """

    :return:
    """
    return global_var.Request_Data

def get_Expect_col():
    """
    期望结果列
    :return:
    """
    return global_var.Expect

def get_Result_col():
    """
    返回实际结果列数
    :return:
    """
    return global_var.Result

def get_Response_data_col():
    """
    返回响应数据列数
    :return:
    """
    return global_var.Response_data


def get_IS_RUn_col():
    """

    :return:
    """
    return global_var.Is_Run

def get_Authorization_col():
    return global_var.Authorization
