# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     write_excel
   Description :
   Author :      'xxxxx'
   date：          2018/8/18
-------------------------------------------------
   Change Activity:
                   2018/8/18:
-------------------------------------------------

封装一个写入Excel的方法，
接收的参数有：'测试编号', '请求方式', 'URL', '请求参数', '预期结果', '是否通过'

"""
__author__ = 'xxxx'

import xlwt
from comm.read_excel import ExcelUtil
from utils.settings import path_file



execl = ExcelUtil(path_file + "\\auto_test_hrm_demo\\test_data\\demo.xlsx","Sheet1")
result = (execl.dict_data())
print(len(result))

writebook = xlwt.Workbook()
sheet = writebook.add_sheet('test')

headList = ['测试编号', '请求方式', 'URL', '请求参数', '预期结果', '是否通过']
for j in range(len(headList)):
    sheet.write(0, j, headList[j])

def write_excel(i,through):
    print(result[i])
    sheet.write(i+1, 0, result[i]['测试编号'])
    sheet.write(i+1, 1, result[i]['请求方式'])
    sheet.write(i+1, 2, result[i]['URL'])
    sheet.write(i+1, 3, result[i]['请求参数'])
    sheet.write(i+1, 4, result[i]['预期结果'])
    sheet.write(i+1, 5, through)

    writebook.save(path_file+'\\auto_test_hrm_demo\\result_data\\answer.xls')



if __name__ == '__main__':
    pass
# import os
# print(os.getcwd())
# print(os.path.abspath('.'))#获得当前工作目录
# print(os.path.abspath('..'))#获得当前工作目录的父目录
# print(os.path.abspath(os.curdir))#获得当前工作目录