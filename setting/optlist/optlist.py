# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/29 11:33
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : optlist.py
# @Software : PyCharm

from config.sem_login.sem_login import Sem_Login_Test as slt
from time import sleep
from params.sem_params import ParamsTest


class SemOptList:

    def __init__(self):
        """
        运营管理系统
        供应链管理
        库存管理  -----   拣货单页面
        """
        self.mm = slt()
        self.urla = ParamsTest().selenium_url_sempreprod()
        self.url = f'{self.urla}scp/inventory/optlist'

    def optlist(self):
        """
        定义driver
        """

        driver = self.mm.sem_login()
        sleep(2)
        driver.get(self.url)

        return driver


if __name__ == '__main__':
    sem = SemOptList()
    sem.optlist()
