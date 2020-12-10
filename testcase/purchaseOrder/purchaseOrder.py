# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 13:15
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : purchaseOrder.py
# @Software : PyCharm
from setting.purchaseOrder.sem_purchaseOrder import Sem_PurchaseOrder
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from time import sleep
import unittest


class PurchaseOrder(unittest.TestCase):

    def setUp(self) -> None:
        spo = Sem_PurchaseOrder()
        self.driver = spo.PurchaseOrder()
        self.wait = WebDriverWait(self.driver, 60)

    def test(self):
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//div[text()='供应链管理']")))
        iframe_test = self.driver.find_element_by_xpath('//*[@id="iframs"]')
        self.driver.switch_to.frame(iframe_test)
        self.wait.until(ec.presence_of_element_located((By.ID, 'purchaseSn')))
        # 输入采购单号
        self.driver.find_element_by_id('purchaseSn').send_keys('CGD202007240001')
        sleep(1)
        # 点击查询
        self.select_test()
        # 操作
        self.driver.find_element_by_xpath("//span[text()='操 作']").click()
        sleep(3)

    def select_test(self):
        # 点击查询
        self.driver.find_element_by_xpath("//span[text()='查 询']").click()

    def tearDown(self) -> None:
        self.driver.quit()
