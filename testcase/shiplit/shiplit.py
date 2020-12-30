# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/30 16:59
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : shiplit.py
# @Software : PyCharm
from setting.shiplit.shiplit import SemShiplit
from time import sleep
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class Shiplit(unittest.TestCase):

    def setUp(self) -> None:
        slow = SemShiplit()
        self.driver = slow.shiplit()
        self.wait = WebDriverWait(self.driver, 60)

    def test(self):
        self.iframe()
        # 发货单号
        self.driver.find_element_by_id('shipmentOrderNo').send_keys('FHD202012301626380054')
        # 关联单号
        self.driver.find_element_by_id('linkedOrderNo').send_keys('NMV202012300037')
        # SKU
        self.driver.find_element_by_id('sku').send_keys('GSPSJ7LBXGSD00001V0')
        # 发货仓库
        self.driver.find_element_by_id('shipmentWarehouse').click()
        self.driver.find_element_by_xpath("(//div[text()='中国仓库'])[2]").click()
        # 发货类型
        self.driver.find_element_by_id('shipmentType').click()
        self.driver.find_element_by_xpath("//div[text()='调仓发货']").click()
        # 单据状态
        self.driver.find_element_by_id('receiptsStatus').click()
        self.driver.find_element_by_xpath("//div[text()='异常完成']").click()
        # 创建日期
        # 开始日期
        data = '2020/12/30'
        self.driver.find_element_by_id('createDate').send_keys(data)
        # 结束日期
        self.driver.find_element_by_xpath("(//input[@placeholder='结束日期'])[1]").send_keys(data)
        # 实际发货日期
        self.driver.find_element_by_id('actualDate').send_keys(data)
        # 结束日期
        self.driver.find_element_by_xpath("(//input[@placeholder='结束日期'])[2]").send_keys(data)

        # 点击查询
        self.select()

        sleep(13)

    def select(self):
        self.driver.find_element_by_xpath("//span[text()='查 询']").click()

    def iframe(self):
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//div[text()='供应链管理']")))
        iframe_test = self.driver.find_element_by_xpath('//*[@id="iframs"]')
        self.driver.switch_to.frame(iframe_test)
        self.wait.until(ec.visibility_of_element_located((By.XPATH, "//th[text()='发货单号']")))

    def tearDown(self) -> None:
        self.driver.quit()
