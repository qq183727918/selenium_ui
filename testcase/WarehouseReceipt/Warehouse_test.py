# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 10:24
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : Warehouse_test.py
# @Software : PyCharm
from typing import Any, Union, Iterable, Container

from setting.WarehouseReceipt.sem_WarehouseReceipt import Sem_WarehouseReceipt
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from params.sem_params import ParamsTest
from time import sleep
import unittest


class WareHouseTest(unittest.TestCase):

    def params(self):
        pams = ParamsTest()
        self.params = pams.purchaseorder()
        return self.params

    def setUp(self) -> None:
        swr = Sem_WarehouseReceipt()

        self.driver = swr.warehouse()

        self.wait = WebDriverWait(self.driver, 60)

    def test(self):
        params = self.params()
        print(params)
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[text()='供应链管理']")))
        iframe_test = self.driver.find_element_by_xpath('//*[@id="iframs"]')
        self.driver.switch_to.frame(iframe_test)
        self.wait.until(expected_conditions.presence_of_element_located((By.ID, 'control-ref_inStockSn')))
        # 输入入库单号
        self.driver.find_element_by_id('control-ref_concatSn').send_keys(params)
        sleep(1)
        # 点击查询
        self.select_test()
        # 勾选
        self.driver.find_element_by_xpath("(//input[@type='checkbox'])[2]").click()
        sleep(1)
        # 点击等待到货
        self.driver.find_element_by_xpath("//span[text()='确认到仓']").click()
        # 点击确认
        self.driver.find_element_by_xpath("//span[text()='保 存']").click()

    def select_test(self):
        # 点击查询
        self.driver.find_element_by_xpath("//button[@type='submit']").click()

    def tearDown(self) -> None:
        self.driver.quit()
