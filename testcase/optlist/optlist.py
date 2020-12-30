# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/30 17:31
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : optlist.py
# @Software : PyCharm

from setting.optlist.optlist import SemOptList
from time import sleep
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class Shiplit(unittest.TestCase):

    def setUp(self) -> None:
        slow = SemOptList()
        self.driver = slow.optlist()
        self.wait = WebDriverWait(self.driver, 60)

    def test(self):
        self.iframe()
        # 拣货单号
        self.driver.find_element_by_id('pickingSn').send_keys('JHD202012301738260043')
        # 关联单号
        self.driver.find_element_by_id('dispatchSn').send_keys('FHD202012301738080056')
        # SKU
        self.driver.find_element_by_id('sku').send_keys('BXXSQGOS580C00001V0')
        # 单据状态
        self.driver.find_element_by_id('status').click()
        self.driver.find_element_by_xpath("//div[text()='待分配']").click()
        # 拣货仓库
        self.driver.find_element_by_id('warehouseId').click()
        self.driver.find_element_by_xpath("//div[text()='中国仓库']").click()
        # 创建日期
        # 开始时间
        self.driver.find_element_by_id('createTime').click()
        self.driver.find_element_by_id('createTime').send_keys('2020-12-29')
        # 结束时间
        self.driver.find_element_by_xpath("(//input[@placeholder='结束日期'])[1]").click()
        self.driver.find_element_by_xpath("(//input[@placeholder='结束日期'])[1]").send_keys('2020-12-31')
        # 拣货完成日
        # 开始时间
        self.driver.find_element_by_id('completedTime').click()
        self.driver.find_element_by_id('completedTime').send_keys('2020-12-31')
        # 结束时间
        self.driver.find_element_by_xpath("(//input[@placeholder='结束日期'])[2]").click()
        self.driver.find_element_by_xpath("(//input[@placeholder='结束日期'])[2]").send_keys('2020-12-31')
        # 点击查询
        self.select()

        sleep(3)

    def select(self):
        self.driver.find_element_by_xpath("//span[text()='查 询']").click()

    def iframe(self):
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//div[text()='供应链管理']")))
        iframe_test = self.driver.find_element_by_xpath('//*[@id="iframs"]')
        self.driver.switch_to.frame(iframe_test)
        self.wait.until(ec.visibility_of_element_located((By.XPATH, "//th[text()='拣货单号']")))

    def tearDown(self) -> None:
        self.driver.quit()
