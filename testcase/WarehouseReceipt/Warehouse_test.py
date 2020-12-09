# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 10:24
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : Warehouse_test.py
# @Software : PyCharm
from setting.WarehouseReceipt.sem_WarehouseReceipt import Sem_WarehouseReceipt
from time import sleep
import unittest


class WareHouseTest(unittest.TestCase):

    def setUp(self) -> None:
        sw = Sem_WarehouseReceipt()
        global driver
        driver = sw.warehouse()

    def test(self):
        driver.minimize_window()
        sleep(10)

    def tearDown(self) -> None:
        driver.quit()
