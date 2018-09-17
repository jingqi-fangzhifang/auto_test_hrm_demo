# auto_test_hrm_demo
本框架基于virtualenv+unittest+requests+HTMLTestRunner自动化测试
python 版本为3.6
virtualenv 安装方式为：pip3 install virtualenv
虚拟环境的安装为：
virtualenv -p c:\python27\python.exe venv #python2
virtualenv -p c:\python36\python.exe venv #python3

激活虚拟环境
activate venv
停止虚拟环境
deactivate
删除虚拟环境
直接删除目录即可.
rmvirtualenv venv

requests是需要手动安装：pip3 install requests 
unittest 是python安装后自带的库不用手动安装  
HTMLTestRunner  需要手动下载，放置到python能查找的目录即可  下载地址：https://github.com/findyou/HTMLTestRunnerCN

目录结构：
---auto_test_hrm_demo
	|__comm
	|	|_read_excel.py      读取Excel
	|	|_requests_test.py   调用_read_excel发送请求
	|	|_write_excel.py     写入Excel
	|_result_data  
	|	|_answer.xls         测试结果Excel
	|_TestCase
	|	|__test_case_demo    测试接口demo
	|_test_data
	|	|_测试数据demo      测试数据
	|_test_reporter         测试报告存放目录
	|	|_测试报告
	|_utils
	|	|_工具
	|_其他文件
	
	
