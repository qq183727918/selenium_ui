# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/11 18:13
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : warehousereceipt.py
# @Software : PyCharm
from params.sem_params import ParamsTest
from setting.WarehouseReceipt.sem_WarehouseReceipt import Sem_WarehouseReceipt
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import sleep


class WareHouseTest:

    def params_ams(self):
        palms = ParamsTest()

        self.params = palms.warehousereceipt()

        return self.params

    def waretest(self):
        swr = Sem_WarehouseReceipt()

        self.driver = swr.warehouse()

        self.wait = WebDriverWait(self.driver, 60)

    # 入库单确认到仓
    def confirmArrival(self):
        params = self.params()

        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[text()='供应链管理']")))

        iframe_test = self.driver.find_element_by_xpath('//*[@id="iframs"]')
        self.driver.switch_to.frame(iframe_test)
        self.wait.until(expected_conditions.presence_of_element_located((By.ID, 'control-ref_inStockSn')))
        # 输入关联单号（采购单）
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
        sleep(2)

    def select_test(self):
        # 点击查询
        self.driver.find_element_by_xpath("//button[@type='submit']").click()

    # 入库单部分完成
    def partialStorage(self):

        self.driver.find_element_by_xpath('').click()

    # 入库单已完成
    def completed(self):
        self.driver.find_element_by_xpath('').click()

    # 入库单异常完成
    def abnormalCompletion(self):
        self.driver.find_element_by_xpath('').click()

    # 入库单生成上架单
    def generateList(self):
        self.driver.find_element_by_xpath('').click()








