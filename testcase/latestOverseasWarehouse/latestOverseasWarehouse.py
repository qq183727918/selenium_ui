# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 13:16
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : latestOverseasWarehouse.py
# @Software : PyCharm
from setting.latestOverseasWarehouse.sem_latestOverseasWarehouse import Sem_LatestOverseasWarehouse
from time import sleep
import unittest


class LatestOverseasWarehouse(unittest.TestCase):

    def setUp(self) -> None:
        slow = Sem_LatestOverseasWarehouse()
        global driver
        driver = slow.LatestOverseasWarehouse()

    def test(self):
        driver.minimize_window()
        sleep(3)

    def tearDown(self) -> None:
        driver.quit()
