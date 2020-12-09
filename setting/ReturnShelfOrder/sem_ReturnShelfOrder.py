# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 9:29
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : sem_ReturnShelfOrder.py
# @Software : PyCharm
from config.ReturnShelfOrder.sem_login import Sem_Login_Test as slt
from time import sleep


class Sem_ReturnShelfOrder:

    def __init__(self):
        '''
        运营管理系统
        供应链管理
        库存管理
        入库单管理  -----   打开返架单页面
        '''
        self.url = 'http://sem.test.vevor.net/scp/Inventory/ReturnShelfOrder'

    def ReturnShelfOrder(self):
        '''
        定义driver 
        '''''
        self.ro = slt()

        driver = self.ro.sem_login()
        sleep(2)
        driver.get(self.url)

        return driver


if __name__ == '__main__':
    sem = Sem_ReturnShelfOrder()
    sem.ReturnShelfOrder()
