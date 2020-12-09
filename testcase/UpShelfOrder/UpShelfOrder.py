# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 13:15
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : UpShelfOrder.py
# @Software : PyCharm
from setting.UpShelfOrder.sem_UpShelfOrder import Sem_UpShelfOrder
from time import sleep
import unittest


class UpShelfOrder(unittest.TestCase):

    def setUp(self) -> None:
        suso = Sem_UpShelfOrder()
        global driver
        driver = suso.UpShelfOrder()

    def test(self):
        driver.minimize_window()
        sleep(10)

    def tearDown(self) -> None:
        driver.quit()
