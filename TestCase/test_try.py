# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_get_list
   Description :
   Author :      ''
   date：          2018/8/20
-------------------------------------------------
   Change Activity:
                   2018/8/20:
-------------------------------------------------
通过读取Excel文件中的数据，自动识别请求方式发送请求，并将测试结果写入到Excel中

"""
__author__ = ''


import unittest
from comm.write_excel import *
from utils.settings import path_file
from comm.read_excel import ExcelUtil
from comm.requests_test import receive_msg
from log_log import Log

log = Log()

class TestGetList(unittest.TestCase):

	def setUp(self):
		execl = ExcelUtil(path_file+"\\auto_test_hrm_demo\\test_data\\demo.xlsx")
		result = (execl.dict_data())

	def test_get(self):

		finally_result,result_response = receive_msg()
		for i in range(len(finally_result)):
			if finally_result[i][0] == finally_result[i][1]:
				self.assertEqual(finally_result[i][0], finally_result[i][1])
				write_excel(i, through='是')
				#print('测试通过')
			else:
				write_excel(i, through='否')
				log.info("请求的实际结果为{}，预期结果为{}".format(finally_result[i][0],finally_result[i][i]))
				log.info("请求的实际结果如下：")
				log.info(result_response)
				self.assertEqual(finally_result[i][0], finally_result[i][1])
				#print('测试不通过')





if __name__ == '__main__':

	unittest.main()




