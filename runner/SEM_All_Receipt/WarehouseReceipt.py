# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 16:17
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : WarehouseReceipt.py
# @Software : PyCharm
import unittest
import HTMLTestRunner1
import time

path = r'D:\Tools\git\selenium_ui\testcase\WarehouseReceipt'
file_path = r'D:\Tools\git\selenium_ui\report\WarehouseReceipt'

# 自动生成测试套件
suite = unittest.defaultTestLoader.discover(fr"{path}", pattern='*.py')

# 定义测试报告文件对象
file = open(fr'{file_path}\Warehouse{time.strftime("%Y-%m-%d")}.html', 'wb')

# 生成运行器
runner = HTMLTestRunner1.HTMLTestRunner(file, title='TestReport', description='SEM_TestReport')

# 运行
runner.run(suite)

# 关闭文件
file.close()
