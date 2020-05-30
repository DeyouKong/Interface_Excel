# -*- coding: utf-8 -*-

__author__ = "Sampson"


import unittest
from Api_Auto_Test.common.HTMLReport import BeautifulReport
import time
import os

current_path = os.getcwd()
report_path = os.path.join(current_path, "logs")
filename = "自动化测试报告_" + time.strftime('%Y-%m-%dT%H%M%S') + ".html"
description='接口自动化测试'

filePath = os.path.join(report_path, filename)
print(filePath)

class TestMethod(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("类执行之前的方法")

    @classmethod
    def tearDownClass(cls):
        print("类执行之后的方法")

    """每次方法之前执行"""
    def setUp(self):
        print("test--->setUp")

    """每次方法之后执行"""
    def tearDown(self):
        print("test-->tearDown")


    def test_01(self):
        """第二个测试用例"""
        print("这是第一个测试方法")

    def test_02(self):
        """第一个测试用例"""
        print("这是第二个测试方法")


if __name__ == '__main__':
    # unittest.main()

    suite = unittest.TestSuite()
    suite.addTest(TestMethod("test_01"))
    # suite.addTest(TestMethod("test_02"))

    # 使用 BeautifulReport
    result = BeautifulReport(suite)
    result.report(
        filename=filename,
        description=description,
        report_dir=filePath
    )

    # # 使用HTMLTestRunner
    # fp = open(filePath, "wb")
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="哈哈", description = u"用例执行情况")
    # runner.run(suite)
    # fp.close()

