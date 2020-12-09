# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 13:15
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : procurementTransit.py
# @Software : PyCharm
from setting.procurementTransit.sem_procurementTransit import Sem_ProcurementTransit
from time import sleep
import unittest


class ProcurementTransit(unittest.TestCase):

    def setUp(self) -> None:
        spt = Sem_ProcurementTransit()
        global driver
        driver = spt.ProcurementTransit()

    def test(self):
        driver.minimize_window()
        sleep(3)

    def tearDown(self) -> None:
        driver.quit()
