# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 9:29
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : sem_purchaseOrder.py
# @Software : PyCharm
from config.purchaseOrder.sem_login import Sem_Login_Test as slt
from time import sleep
from params.sem_params import ParamsTest

class Sem_PurchaseOrder:

    def __init__(self):
        """
        运营管理系统
        供应链管理
        库存管理
        入库单管理  -----   打开采购单页面
        """
        self.urla = ParamsTest().seleniumurl()
        self.url = f'{self.urla}scp/purchase/purchaseOrder'

    def PurchaseOrder(self):
        """
        定义driver
        """
        self.po = slt()

        driver = self.po.sem_login()
        sleep(2)
        driver.get(self.url)

        return driver


if __name__ == '__main__':
    sem = Sem_PurchaseOrder()
    sem.PurchaseOrder()
