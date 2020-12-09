# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 13:15
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : purchaseOrder.py
# @Software : PyCharm
from setting.purchaseOrder.sem_purchaseOrder import Sem_PurchaseOrder
from time import sleep
import unittest


class PurchaseOrder(unittest.TestCase):

    def setUp(self) -> None:
        spo = Sem_PurchaseOrder()
        global driver
        driver = spo.PurchaseOrder()

    def test(self):
        driver.minimize_window()
        sleep(3)

    def tearDown(self) -> None:
        driver.quit()
