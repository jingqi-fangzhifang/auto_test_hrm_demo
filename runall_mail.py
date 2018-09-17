#!/usr/bin/env python
#-- coding: utf-8 --

"""
author = 'jingqi'

mtime = '2018/4/16'



# coding:utf-8
'''Start all check ,generate reports and then send email

'''

import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from utils.common import send_mail

# 查找测试目录，找到最新生成的测试报告

def new_report(test_report):

    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + '\\' + fn))
    file_new = os.path.join(test_report, lists[-1])
    return file_new


if __name__ == "__main__":

    test_dir = os.path.abspath(os.path.dirname(__file__))
    print(test_dir)
    test_report = test_dir + "\\test_reporter"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    # 定义报告存放路径
    filename = test_report + "\\" + now + 'result.html'
    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title=u"自动生成测试报告",
                            description=u"每个接口的调用情况:")
    # 运行测试
    runner.run(discover)
    fp.close()  # 关闭报告文件

    new_report = new_report(test_report)
    send_mail(new_report)
