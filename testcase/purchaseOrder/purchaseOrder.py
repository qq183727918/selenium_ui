# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 13:15
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : purchaseOrder.py
# @Software : PyCharm
from setting.purchaseOrder.sem_purchaseOrder import Sem_PurchaseOrder
# from selenium.webdriver.common.keys import Keys
from params.sem_params import ParamsTest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from time import sleep
import unittest


class PurchaseOrderTets(unittest.TestCase):

    def setUp(self) -> None:
        spo = Sem_PurchaseOrder()
        self.driver = spo.PurchaseOrder()
        self.wait = WebDriverWait(self.driver, 60)

    def test(self):
        # 查询采购单
        self.select_test()
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//span[text()='操 作']")))
        # 操作
        self.driver.find_element_by_xpath("//span[text()='操 作']").click()
        sleep(1)
        # 编辑
        self.driver.find_element_by_xpath("//span[text()='编 辑']").click()
        sleep(1)
        # 关闭
        self.driver.find_element_by_xpath('//*[@class="ant-modal-close-x"]/span').click()
        # 操作
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//span[text()='操 作']")))
        self.driver.find_element_by_xpath("//span[text()='操 作']").click()
        sleep(1)
        # 拆分
        self.driver.find_element_by_xpath("//span[text()='拆 分']").click()
        sleep(1)

    def select_test(self):
        purchase = ParamsTest()
        purchases = purchase.purchaseorder()
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//div[text()='供应链管理']")))
        iframe_test = self.driver.find_element_by_xpath('//*[@id="iframs"]')
        self.driver.switch_to.frame(iframe_test)
        self.wait.until(ec.presence_of_element_located((By.ID, 'purchaseSn')))
        # 输入采购单号
        self.driver.find_element_by_id('purchaseSn').send_keys(purchases)
        sleep(1)
        # 点击查询
        self.driver.find_element_by_xpath("//span[text()='查 询']").click()


    def tearDown(self) -> None:
        self.driver.quit()
