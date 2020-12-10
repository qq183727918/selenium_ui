# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 9:29
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : sem_WarehouseReceipt.py
# @Software : PyCharm
from config.WarehouseReceipt.sem_login import Sem_Login_Test as slt
from time import sleep
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

class Sem_WarehouseReceipt:

    def __init__(self):
        '''
        运营管理系统
        供应链管理
        库存管理
        入库单管理  -----   打开入库单页面
        '''
        self.url = 'http://sem.test.vevor.net/scp/Inventory/WarehouseReceipt'

    def warehouse(self):
        '''
        定义driver 
        '''''
        self.swhr = slt()
        driver = self.swhr.sem_login()
        sleep(2)
        driver.get(self.url)

        return driver


if __name__ == '__main__':
    sem = Sem_WarehouseReceipt()
    sem.warehouse()
