# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 13:15
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : ReturnShelfOrder.py
# @Software : PyCharm
from setting.ReturnShelfOrder.sem_ReturnShelfOrder import Sem_ReturnShelfOrder
from time import sleep
import unittest


class ReturnShelfOrder(unittest.TestCase):

    def setUp(self) -> None:
        srso = Sem_ReturnShelfOrder()
        global driver
        driver = srso.ReturnShelfOrder()

    def test(self):
        driver.minimize_window()
        sleep(10)

    def tearDown(self) -> None:
        driver.quit()
