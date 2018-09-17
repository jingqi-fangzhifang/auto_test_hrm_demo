# # -*- coding: utf-8 -*-
# __author__ = '测试景麒'

'''
封装一个方法，通过调用read_excel中的类中的方法来实现自动识别请求方式发送请求校验接口结果
'''



from comm.read_excel import ExcelUtil
import requests
from utils.settings import headers,path_file
import json
from log_log import Log

log = Log()

execl = ExcelUtil(path_file+"\\auto_test_hrm_demo\\test_data\\demo.xlsx")
result = (execl.dict_data())


def receive_msg():
	log.info("---测试开始----")
	results = []
	for i in range(len(result)):
		test_num = result[i]['测试编号']
		request_way = result[i]['请求方式']
		request_URL = result[i]['URL']
		request_parameters = result[i]['请求参数']
		if request_parameters == '':
			pass
		else:
			request_parameters = eval(request_parameters)
		expected_results = result[i]['预期结果']

		print('测试编号',test_num)

		#res.append((test_num, request_way, request_URL, request_parameters, expected_results))
		print((request_parameters))
		actual_result,result_response = send_request(url=request_URL, request_way=request_way, data=request_parameters)

		results.append((actual_result,expected_results, i))


	return (results,result_response)


def send_request(url, request_way, data):
	if request_way == 'get':
		res = requests.get(url, headers=headers, data=data)
		response = res.text
	if request_way == 'post':
		res = requests.post(url, headers=headers, data=data)
		response = res.text
		#log.info(response)
	try:
		data = json.loads(response)
		actual_results = data['success']
	except Exception as e:
		data = json.loads(response)
		actual_results = data['status']
		log.info('错误信息>>>{}'.format(e))
	if actual_results == True:
		actual_results = '接口请求正常'
	else:
		actual_results = '接口请求异常'
	return (actual_results,response)


if __name__ == '__main__':
	print(receive_msg())
	print(1111)