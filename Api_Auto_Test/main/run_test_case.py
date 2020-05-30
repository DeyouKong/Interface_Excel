# -*- coding: utf-8 -*-

# @File: run_test_case
# @Author : "Sampson"
# @Detail :

from Api_Auto_Test import *
import platform

case_path = '/TestCase' if platform.system() != 'Windows' else '\TestCase'

report_path = '/TestFiles/TestReport' if platform.system() != 'Windows' else '\TestFiles\TestReport'

test_case_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0] + case_path
test_report_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0] + report_path


if __name__ == '__main__':

    nowTime = datetime.strftime(datetime.now(), '%Y-%m-%d_%H_%M_%S')
    result = BeautifulReport(unittest.defaultTestLoader.discover(test_case_path,"Case_*.py"))
    result.report(
        filename="Case_" + nowTime + '自动化测试报告',
        description='接口自动化测试',
        report_dir=test_report_path,
    )