# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/29 14:07
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : transfer.py
# @Software : PyCharm
from setting.transfer.transfer import Semtransfer
from time import sleep
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class Transfer(unittest.TestCase):

    def setUp(self) -> None:
        slow = Semtransfer()
        self.driver = slow.transfer()
        self.wait = WebDriverWait(self.driver, 60)

    def test(self):
        self.iframe()
        # 调仓单号
        self.driver.find_element_by_id('transferInventoryCode').send_keys('NMV202011194404')
        # 采购单号
        self.driver.find_element_by_id('purchaseBillCode').send_keys('NCG2020090926894')
        # 调仓单名称
        self.driver.find_element_by_id('name').send_keys('美国-FBA-SS-MDW8-0064')
        # SKU
        self.driver.find_element_by_id('skuCode').send_keys('1000FTPEXZYG00001V0')
        # 发货仓
        self.driver.find_element_by_id('deliverWarehouse').click()
        self.driver.find_element_by_xpath("(//div[text()='中国仓库'])[2]").click()
        # 收货仓
        warehouse = '美国-FBA-salesupermarket@outlook.com'
        # //span[text()='美国-FBA-salesupermarket@outlook.com']
        self.driver.find_element_by_id('receiveWarehouse').send_keys(warehouse)
        self.driver.find_element_by_xpath(f"//span[text()='{warehouse}']").click()
        # 创建时间
        # 开始日期
        self.driver.find_element_by_xpath("//input[@placeholder='开始日期']").send_keys('2020-12-29')
        # 结束日期
        self.driver.find_element_by_xpath("//input[@placeholder='结束日期']").click()
        self.driver.find_element_by_xpath("//input[@placeholder='结束日期']").send_keys('2020-12-30')
        self.driver.find_element_by_xpath("(//div[text()='30'])[2]").click()

        # 点击查询
        self.select()

        sleep(13)

    def select(self):
        self.driver.find_element_by_xpath("//span[text()='查 询']").click()

    def timeFrame(self, fraem):
        self.driver.find_element_by_xpath(f"//span[text()='{fraem}']").click()

    def iframe(self):
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//div[text()='供应链管理']")))
        iframe_test = self.driver.find_element_by_xpath('//*[@id="iframs"]')
        self.driver.switch_to.frame(iframe_test)
        self.wait.until(ec.visibility_of_element_located((By.XPATH, "//th[text()='调仓单号']")))

    def frames(self, period):
        self.wait.until(ec.visibility_of_element_located((By.XPATH, f"//div[text()='{period}']")))
        print()

    def tearDown(self) -> None:
        self.driver.quit()
