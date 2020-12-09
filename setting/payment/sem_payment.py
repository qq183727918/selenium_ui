# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 9:29
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : sem_payment.py
# @Software : PyCharm
from config.payment.sem_login import Sem_Login_Test as slt
from time import sleep


class Sem_Payment:

    def __init__(self):
        '''
        运营管理系统
        供应链管理
        库存管理
        入库单管理  -----   打开付款单页面
        '''
        self.url = 'http://sem.test.vevor.net/scp/purchase/payment'

    def Payment(self):
        '''
        定义driver 
        '''''
        self.pay = slt()

        driver = self.pay.sem_login()
        sleep(2)
        driver.get(self.url)

        return driver


if __name__ == '__main__':
    sem = Sem_Payment()
    sem.Payment()
