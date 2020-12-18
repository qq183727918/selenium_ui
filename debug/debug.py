# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 10:31
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : debug.py
# @Software : PyCharm

from influence.payment.payment import PayMent

sem = PayMent()
noTicketToPay = sem.paymentest()[0]
ticketToPayment = sem.paymentest()[1]
print(noTicketToPay)
print(ticketToPayment)
