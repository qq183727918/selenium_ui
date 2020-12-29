# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 9:29
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : sem_latestOverseasWarehouse.py
# @Software : PyCharm
from config.sem_login.sem_login import Sem_Login_Test as slt
from time import sleep
from params.sem_params import ParamsTest


# noinspection PyPep8Naming
class Sem_LatestOverseasWarehouse:

    def __init__(self):
        """
        运营管理系统
        供应链管理
        库存管理
        入库单管理  -----   打开最新海外仓页面
        """
        self.urla = ParamsTest().url_test()
        self.url = f'{self.urla}scp/purchase/latestOverseasWarehouse'

    # noinspection PyPep8Naming
    def LatestOverseasWarehouse(self):
        '''
        定义driver 
        '''''
        self.low = slt()

        driver = self.low.sem_login()
        sleep(2)
        driver.get(self.url)

        return driver


if __name__ == '__main__':
    sem = Sem_LatestOverseasWarehouse()
    sem.LatestOverseasWarehouse()
