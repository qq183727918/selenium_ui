# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 9:29
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : sem_UpShelfOrder.py
# @Software : PyCharm
from config.UpShelfOrder.sem_login import Sem_Login_Test as slt
from time import sleep
from params.sem_params import ParamsTest

class Sem_UpShelfOrder:

    def __init__(self):
        '''
        运营管理系统
        供应链管理
        库存管理
        入库单管理  -----   打开上架单页面
        '''
        self.urla = ParamsTest().seleniumurl()
        self.url = f'{self.urla}scp/Inventory/UpShelfOrder'

    def UpShelfOrder(self):
        '''
        定义driver 
        '''''
        self.uso = slt()

        driver = self.uso.sem_login()
        sleep(2)
        driver.get(self.url)

        return driver


if __name__ == '__main__':
    sem = Sem_UpShelfOrder()
    sem.UpShelfOrder()
