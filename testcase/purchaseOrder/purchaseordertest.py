# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/17 21:55
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : purchaseordertest.py
# @Software : PyCharm

from influence.payment.payment import PayMent
from influence.purchaseOrder.purchaseorder import PurchaseOrderParams

# 付款单
sempayment = PayMent()
semp = sempayment.paymentest()
# 无票可付
noTicketToPay = semp[0]
# 票到付款
ticketToPayment = semp[1]

# 采购单
sempurchaseorder = PurchaseOrderParams()
sempo = sempurchaseorder.orderparams()
# 采购总价
pirc = sempo[0]
# 是否含税
tax = sempo[1]
# 供应商ID
procurementSupplierId = sempo[2]
# 采购单订单类型
orderType = sempo[3]
# 票到付尾款
finalPaymentOnDelivery = 0
# 限制金额
limitAmount = 0
# 判断该采购单该生成的付款单类型以及数量
if tax == 0:  # 含税
    if orderType == 0 or orderType == 3:
        # 一笔无票可付
        if noTicketToPay == 1 and ticketToPayment == 0:
            print('采购单生成付款单正确')
        else:
            print('采购单生成的付款单不正确')
    else:
        if pirc > 5000:
            # 第一笔第二笔合成一笔无票可付，第三笔无票可付
            if noTicketToPay == 2 and ticketToPayment == 0:
                print('采购单生成付款单正确')
            else:
                print('采购单生成的付款单不正确')
        elif pirc <= 5000:
            # 一笔无票可付
            if noTicketToPay == 1 and ticketToPayment == 0:
                print('采购单生成付款单正确')
            else:
                print('采购单生成的付款单不正确')

elif tax == 1:  # 不含税
    # 配件单与样品单
    if orderType == 0 or orderType == 3:
        # 一笔无票可付
        if noTicketToPay == 1 and ticketToPayment == 0:
            print('采购单生成付款单正确')
        else:
            print('采购单生成的付款单不正确')
    else:
        if pirc >= 5000:
            # 判断是否票到付尾款
            if finalPaymentOnDelivery == 0:  # 0是，票到付尾款
                # 一笔无票可付，第两笔第三笔票到付款
                if noTicketToPay == 1 and ticketToPayment == 2:
                    print('采购单生成付款单正确')
                else:
                    print('采购单生成的付款单不正确')
            elif finalPaymentOnDelivery == 1:  # 1否，票到付尾款
                if pirc < limitAmount:  # 小于限制金额
                    # 一笔无票可付
                    if noTicketToPay == 1 and ticketToPayment == 0:
                        print('采购单生成付款单正确')
                    else:
                        print('采购单生成的付款单不正确')
                else:   # 大于等于限制金额
                    # 第一笔第二笔合成一笔无票可付  第三笔生成票到付款
                    if noTicketToPay == 1 and ticketToPayment == 0:
                        print('采购单生成付款单正确')
                    else:
                        print('采购单生成的付款单不正确')
            else:
                print('采购单生成的付款单不正确')
        elif pirc < 5000:
            # 无票可付
            if noTicketToPay == 1 and ticketToPayment == 0:
                print('采购单生成付款单正确')
            else:
                print('采购单生成的付款单不正确')
        else:
            print('采购价错误')
else:
    print('是否含税类型错误')
