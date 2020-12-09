# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 13:37
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : Sem_All_Receipt.py
# @Software : PyCharm
import unittest
import HTMLTestRunner1
import time
from ddt import file_data, ddt

@ddt
class RunnerTest(unittest.TestCase):

    @file_data(r'D:\Tools\git\selenium_ui\Yaml\SEM_All_Receipt\SEM_All_Receipt.yaml')

    def test_runner(self,path, file_path):

        print(path, file_path)

        # 自动生成测试套件
        suite = unittest.defaultTestLoader.discover(path, pattern='*.py')

        # 定义测试报告文件对象
        file = open(f'{file_path}_{time.strftime("%Y-%m-%d")}.html', 'wb')

        # 生成运行器
        runner = HTMLTestRunner1.HTMLTestRunner(file, title='TestReport', description='SEM_TestReport')

        # 运行
        runner.run(suite)

        # 关闭文件
        file.close()


if __name__=='__main__':
    unittest.main()
