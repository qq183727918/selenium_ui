# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 16:26
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : run.py
# @Software : PyCharm
import os
from time import sleep

os.system(r'python D:\Tools\git\selenium_ui\runner\SEM_All_Receipt\latestOverseasWarehouse.py')
sleep(1)
os.system(r'python D:\Tools\git\selenium_ui\runner\SEM_All_Receipt\MoveMoney.py')
sleep(1)
os.system(r'python D:\Tools\git\selenium_ui\runner\SEM_All_Receipt\payment.py')
sleep(1)
os.system(r'python D:\Tools\git\selenium_ui\runner\SEM_All_Receipt\procurementTransit.py')
sleep(1)
os.system(r'python D:\Tools\git\selenium_ui\runner\SEM_All_Receipt\purchaseOrder.py')
sleep(1)
os.system(r'python D:\Tools\git\selenium_ui\runner\SEM_All_Receipt\ReturnShelfOrder.py')
sleep(1)
os.system(r'python D:\Tools\git\selenium_ui\runner\SEM_All_Receipt\UpShelfOrder.py')
sleep(1)
os.system(r'python D:\Tools\git\selenium_ui\runner\SEM_All_Receipt\WarehouseReceipt.py')
sleep(1)
