# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 13:16
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : MoveMoney.py
# @Software : PyCharm
from setting.MoveMoney.sem_MoveMoney import Sem_MoveMoney
from time import sleep
import unittest


class MoveMoney(unittest.TestCase):

    def setUp(self) -> None:
        smm = Sem_MoveMoney()
        global driver
        driver = smm.MoveMoney()

    def test(self):
        driver.minimize_window()
        sleep(10)

    def tearDown(self) -> None:
        driver.quit()
