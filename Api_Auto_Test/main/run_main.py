# -*- coding: utf-8 -*-

# @File: run_main
# @Author : "Sampson"
# @Detail :
# @time :
import os
import sys
import json

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from Api_Auto_Test.common.runMethod import RunMethod
from Api_Auto_Test.common.data.get_data_excel import Get_Data
from Api_Auto_Test.common import checkResult
from Api_Auto_Test.common.data import depend_data
from Api_Auto_Test.common.sendMail import sendMail


class RunTest(object):
    __doc__ = " 程序主函数入口 "

    def __init__(self):
        self.run_method = RunMethod()
        self.data = Get_Data()
        self.check_result = checkResult.checkResult()

    def get_run_data(self, row):
        host = self.data.get_Host(row)
        url = host + self.data.get_request_url(row)
        method = self.data.get_request_method(row)
        is_run = self.data.get_is_run(row)
        data = self.data.get_request_data(row)
        header = self.data.get_header(row)
        except_data = self.data.get_except_data(row)
        case_depend = self.data.get_case_depend(row)
        if case_depend:
            """获取数据依赖字段对应的值，更新字段依赖中值"""
            caseDepend = depend_data.depend_Data(case_depend)
            data_depend_response_data = caseDepend.get_data_for_case_depend_key(row)
            field_depend = self.data.get_field_depend(row)
            data[field_depend] = data_depend_response_data

        return url, method, is_run, data, header, except_data

    def checkResult(self, row, res):
        except_msg = self.data.get_except_data(row)

    def go_run(self):
        rows_count = self.data.get_excel_lines()
        run_count = 0
        success_count = 0
        fail_count = 0
        for row in range(1, rows_count):
            res = None
            url, method, is_run, data, header, except_data = self.get_run_data(row)
            print(url, method, is_run, data, header, except_data)
            if is_run:
                run_count += 1
                res = self.run_method.run_main(method, url, data, header)
                print(type(res))
                if self.check_result.is_contain(except_data, res):
                    self.data.write_result(row, value="pass")
                    success_count += 1
                    if "/api/service-upms/admin/user/login" in url:
                        res = json.loads(res)
                        Authorization = "Bearer" + res["data"]["token"]
                        self.data.write_result(row, Authorization=Authorization,)
                else:
                    self.data.write_result(row, value="fail", res=res)
                    fail_count += 1
        pass_percent = "%.2f%%" %(success_count/run_count*100)
        send_mail = sendMail()
        main_msg = "执行用例数：{}\n" \
                   "成功数：{}\n" \
                   "失败数：{}\n" \
                   "通过率：{}".format(run_count,success_count,fail_count,pass_percent)
        send_mail.send_mail(main_msg=main_msg, file=1)
        send_mail.close()



if __name__ == '__main__':
    run = RunTest()
    res = run.go_run()
    # print(res)
