# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 13:16
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : payment.py
# @Software : PyCharm
from setting.payment.sem_payment import Sem_Payment
from time import sleep
import unittest


class Payment(unittest.TestCase):

    def setUp(self) -> None:
        sp = Sem_Payment()
        global driver
        driver = sp.Payment()

    def test(self):
        driver.minimize_window()
        sleep(10)

    def tearDown(self) -> None:
        driver.quit()
