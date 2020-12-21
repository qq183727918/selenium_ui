# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 8:54
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : sem_login.py
# @Software : PyCharm
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from params.sem_params import ParamsTest


class Sem_Login_Test:

    def __init__(self):
        """
        运营管理系统  -----   登录操作
        供应链管理
        库存管理
        入库单管理
        """
        self.urla = ParamsTest().seleniumurl()

        self.url = f'{self.urla}login'

        self.name = 'liuxiaoqiang'

        self.pwd = '!sishun666'

        self.name_id = 'username'

        self.pwd_id = 'password'

        self.login = '//*[@type="button"]'
        self.driver = webdriver.Chrome()

    def sem_login(self):
        '''
        设置driver可以全局调用
        '''
        driver = self.driver
        wait = WebDriverWait(driver, 60)
        driver.maximize_window()
        driver.get(self.url)
        wait.until(EC.presence_of_element_located((By.ID, self.name_id)))
        driver.find_element_by_id(self.name_id).send_keys(self.name)
        sleep(0.5)
        driver.find_element_by_id(self.pwd_id).send_keys(self.pwd)
        sleep(0.5)
        driver.find_element_by_xpath(self.login).click()
        sleep(0.5)

        # driver.get('http://sem.test.vevor.net/scp/Inventory/WarehouseReceipt')
        # sleep(5)
        return driver


if __name__ == '__main__':
    slt = Sem_Login_Test()
    slt.sem_login()
