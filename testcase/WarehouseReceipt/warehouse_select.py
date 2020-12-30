# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/30 19:11
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : warehouse_select.py
# @Software : PyCharm

from setting.WarehouseReceipt.sem_WarehouseReceipt import Sem_WarehouseReceipt
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import unittest
from time import sleep


class WareHouseTest(unittest.TestCase):

    def setUp(self) -> None:
        slow = Sem_WarehouseReceipt()
        self.driver = slow.warehouse()
        self.wait = WebDriverWait(self.driver, 60)

    def test(self):
        self.iframe()
        # 入库单号
        self.driver.find_element_by_id('control-ref_inStockSn').send_keys('NDH202012204071')

        # 单据状态
        self.driver.find_element_by_id("control-ref_inStockStatus").send_keys('已完成')
        self.driver.find_element_by_xpath("//div[text()='已完成']").click()

        # 创建日期
        # 开始日期
        self.driver.find_element_by_id('control-ref_createdTime').click()
        self.driver.find_element_by_id('control-ref_createdTime').send_keys('2020-12-19')
        # 结束日期
        self.driver.find_element_by_xpath("(//input[@placeholder='结束日期'])[1]").click()
        self.driver.find_element_by_xpath("(//input[@placeholder='结束日期'])[1]").send_keys('2020-12-21')

        # 目的仓库
        # self.driver.find_element_by_xpath("(//span[@class='ant-select-selection-item'])[2]").click()
        # self.driver.find_element_by_xpath("(//span[@class='ant-select-selection-item'])[2]").send_keys('4PX-捷克仓')
        # self.driver.find_element_by_xpath("//div[text()='4PX-捷克仓']").click()

        # 关联单号
        self.driver.find_element_by_id('control-ref_concatSn').send_keys('NCG2020110938546')

        # 预计到仓日
        # 开始日期
        self.driver.find_element_by_id('control-ref_predictWarehouseTime').click()
        self.driver.find_element_by_id('control-ref_predictWarehouseTime').send_keys('2020-12-20')
        # 结束日期
        self.driver.find_element_by_xpath("(//input[@placeholder='结束日期'])[2]").click()
        self.driver.find_element_by_xpath("(//input[@placeholder='结束日期'])[2]").send_keys('2020-12-22')

        # SKU
        self.driver.find_element_by_id('control-ref_sku').send_keys('DLZQGJSHYCT520001V2')

        # 入库类型
        # self.driver.find_element_by_id("control-ref_inStockType").click()
        # self.driver.find_element_by_xpath("//div[text()='采购入库']").click()

        # 预计装柜日
        # 开始日期
        self.driver.find_element_by_id('control-ref_predictLoadingTime').click()
        self.driver.find_element_by_id('control-ref_predictLoadingTime').send_keys('2020-12-27')
        # 结束日期
        self.driver.find_element_by_xpath("(//input[@placeholder='结束日期'])[3]").click()
        self.driver.find_element_by_xpath("(//input[@placeholder='结束日期'])[3]").send_keys('2020-12-29')

        # 小组
        # self.driver.find_element_by_id("control-ref_groupId").click()

        # 供应商
        # self.driver.find_element_by_id("control-ref_supplierId").click()
        # self.driver.find_element_by_xpath("//div[text()='深圳市锐丰焊接设备有限公司']").click()

        # 实际入库日
        # 开始日期
        self.driver.find_element_by_id('control-ref_practicalReceiveTime').click()
        self.driver.find_element_by_id('control-ref_practicalReceiveTime').send_keys('2020-12-28')
        # 结束日期
        self.driver.find_element_by_xpath("(//input[@placeholder='结束日期'])[4]").click()
        self.driver.find_element_by_xpath("(//input[@placeholder='结束日期'])[4]").send_keys('2020-12-30')

        # 是否生成上架单
        # self.driver.find_element_by_xpath("(//span[@class='ant-select-selection-item'])[2]").click()
        # self.driver.find_element_by_xpath("//div[text()='是']").click()

        # 点击查询
        self.select()

        sleep(13)

    def select(self):
        self.driver.find_element_by_xpath("//span[text()='查 询']").click()

    def iframe(self):
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//div[text()='供应链管理']")))
        iframe_test = self.driver.find_element_by_xpath('//*[@id="iframs"]')
        self.driver.switch_to.frame(iframe_test)
        self.wait.until(ec.visibility_of_element_located((By.XPATH, "//th[text()='入库单号']")))

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main':
    pass
