# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 10:31
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : debug.py
# @Software : PyCharm
from setting.WarehouseReceipt.sem_WarehouseReceipt import Sem_WarehouseReceipt
from time import sleep
sw = Sem_WarehouseReceipt()

driver = sw.warehouse()

driver.minimize_window()
sleep(10)
