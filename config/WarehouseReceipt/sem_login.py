# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 8:54
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : sem_login.py
# @Software : PyCharm
from selenium import webdriver
from time import sleep


class Sem_Login_Test:

    def __init__(self):
        '''
        运营管理系统  -----   登录操作
        供应链管理
        库存管理
        入库单管理
        '''
        self.url = 'http://sem.test.vevor.net/'

        self.name = 'liuxiaoqiang'

        self.pwd = '!sishun666'

        self.name_id = 'username'

        self.pwd_id = 'password'

        self.login = '//*[@type="button"]'

    def driver_test(self):
        '''
        设置driver可以全局调用
        '''
        global driver
        driver = webdriver.Chrome()

        return driver

    def sem_login(self):
        driver.get(self.url)
        driver.maximize_window()
        sleep(0.5)
        driver.find_element_by_id(self.name_id).send_keys(self.name)
        sleep(0.5)
        driver.find_element_by_id(self.pwd_id).send_keys(self.pwd)
        sleep(0.5)
        driver.find_element_by_xpath(self.login).click()
        sleep(0.5)

        # driver.get('http://sem.test.vevor.net/scp/Inventory/WarehouseReceipt')
        # sleep(5)


if __name__ == '__main__':
    slt = Sem_Login_Test()
    slt.driver_test()
    slt.sem_login()
