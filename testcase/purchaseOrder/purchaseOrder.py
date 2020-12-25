# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 13:15
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : purchaseOrder.py
# @Software : PyCharm

from selenium.webdriver import ActionChains
from setting.purchaseOrder.sem_purchaseOrder import Sem_PurchaseOrder
from testcase.determine.purchase_payment import JudgePaymentSlip
from selenium.webdriver.common.keys import Keys
from params.sem_params import ParamsTest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from time import sleep
import unittest


class PurchaseOrderTest(unittest.TestCase):

    def setUp(self) -> None:
        spo = Sem_PurchaseOrder()
        self.driver = spo.PurchaseOrder()
        self.wait = WebDriverWait(self.driver, 60)

    def test(self):
        try:
            # 查询采购单
            self.select_test()
            self.wait.until(ec.presence_of_element_located((By.XPATH, f"//span[text()='{self.purchases}']")))
            # 操作
            # self.driver.find_element_by_xpath("//span[text()='操 作']").click()
            # 操作悬停
            move = self.driver.find_element_by_xpath("//span[text()='操作']")
            # 对定位到的元素执行悬停操作
            ActionChains(self.driver).move_to_element(move).perform()
            # 编辑
            self.driver.find_element_by_xpath("//span[text()='编 辑']").click()
            sleep(1)
            # 截图
            self.driver.get_screenshot_as_file(r'D:\Tools\git\selenium_ui\image\purchaseOrder\编辑页面.png')
            # 选择国内收货仓 (//*[@class="ant-select-selector"])[8]
            self.driver.find_element_by_xpath('(//*[@class="ant-select-selector"])[9]').click()
            sleep(0.5)
            self.driver.find_element_by_xpath("//div[text()='中国仓库']").click()
            sleep(0.5)
            # 选择海外仓 (//*[@class="ant-select-selector"])[9]
            # self.driver.find_element_by_xpath('(//*[@class="ant-select-selector"])[9]').click()
            # 清楚输入框
            self.driver.find_element_by_id('domesticRequiredArrivalDate').click()
            self.driver.find_element_by_id('domesticRequiredArrivalDate').send_keys(Keys.CONTROL, 'a')
            self.driver.find_element_by_id('domesticRequiredArrivalDate').send_keys(Keys.BACKSPACE)
            # 国内要求到货日期 domesticRequiredArrivalDate
            self.driver.find_element_by_id('domesticRequiredArrivalDate').send_keys('2020-12-16')
            sleep(0.5)
            # 点击保存
            self.driver.find_element_by_xpath("(//button[@class='ant-btn'])[1]").click()
            sleep(0.5)
            # 点击提交
            self.driver.find_element_by_xpath("(//button[@class='ant-btn'])[2]").click()
            sleep(0.5)
            # 点击厂家接单    生成预付款单
            self.driver.find_element_by_xpath("(//button[@class='ant-btn'])[4]").click()
            sleep(0.5)
            # 点击待发货
            self.driver.find_element_by_xpath("//span[text()='待发货']").click()
            sleep(0.5)
            # 点击已发货   生成入库单
            self.driver.find_element_by_xpath("//span[text()='已发货']").click()
            sleep(0.5)
            # 点击解冻按钮
            self.driver.find_element_by_xpath("//span[text()='解 冻']").click()
            sleep(0.5)
            # 点击冻结
            self.driver.find_element_by_xpath("//span[text()='冻 结']").click()
            sleep(0.5)
            # 点击驳回
            self.driver.find_element_by_xpath("//span[text()='驳 回']").click()
            sleep(0.5)
            # 点击提前到货解锁
            self.driver.find_element_by_xpath("//span[text()='提前到货解锁']").click()
            sleep(0.5)
            # 点击厂家拒单
            self.driver.find_element_by_xpath("//span[text()='提前到货解锁']").click()
            sleep(0.5)
            # 点击生成入库单
            self.driver.find_element_by_xpath("//span[text()='生成入库单']").click()
            sleep(0.5)
            # 点击生成付款单
            self.driver.find_element_by_xpath("//span[text()='生成付款单']").click()
            sleep(0.5)
            # 判断付款单是否生成正确
            JudgePaymentSlip().paymentslip()
            # 关闭
            self.driver.find_element_by_xpath('//*[@class="ant-modal-close-x"]/span').click()
            sleep(1)
        except:
            self.driver.get_screenshot_as_file(r'D:\Tools\git\selenium_ui\image\purchaseOrder\错误.png')

    # 拆分采购单
    def splittest(self):
        # 操作
        self.wait.until(ec.presence_of_element_located((By.XPATH, f"//span[text()='{self.purchases}']")))
        # 操作悬停
        move = self.driver.find_element_by_xpath("//span[text()='操 作']")
        # 对定位到的元素执行悬停操作
        ActionChains(self.driver).move_to_element(move).perform()
        # 拆分
        self.driver.find_element_by_xpath("//span[text()='拆 分']").click()
        sleep(1)
        # 截图
        self.driver.get_screenshot_as_file(r'D:\Tools\git\selenium_ui\image\purchaseOrder\拆分页面.png')

    def select_test(self):
        purchase = ParamsTest()
        self.purchases = purchase.purchaseorder()
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//div[text()='供应链管理']")))
        iframe_test = self.driver.find_element_by_xpath('//*[@id="iframs"]')
        self.driver.switch_to.frame(iframe_test)
        self.wait.until(ec.presence_of_element_located((By.ID, 'purchaseSn')))
        # 输入采购单号
        self.driver.find_element_by_id('purchaseSn').send_keys(self.purchases)
        sleep(1)
        # 点击查询
        self.driver.find_element_by_xpath("//span[text()='查 询']").click()
        sleep(1)

    def tearDown(self) -> None:
        self.driver.quit()
