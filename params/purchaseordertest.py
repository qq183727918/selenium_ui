# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/17 21:55
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : purchaseordertest.py
# @Software : PyCharm

from influence.SupplierManagement.SupplierManagement import SupplierMent
from influence.payment.payment import PayMent
from influence.purchaseOrder.purchaseorder import PurchaseOrderParams
from influence.SupplierManagement.SupplierManagement import SupplierMent

# 付款单
sempayment = PayMent()
semp = sempayment.paymentest()
print(semp)
# 无票可付
noTicketToPay = 0
# 票到付款
ticketToPayment = 0
for i in semp:
    if i["attributeName"] == "无票可付":
        noTicketToPay += 1
    elif i["attributeName"] == "票到付款":
        ticketToPayment += 1
    else:
        print('该属性错误')
print(f'无票可付:{noTicketToPay}')
print(f'票到付款:{ticketToPayment}')

# 采购单
sempurchaseorder = PurchaseOrderParams()
sempo = sempurchaseorder.params()
print(sempo)
# 采购总价
pirc = sempo['采购总价']
# 是否含税
tax = sempo['是否含税']
# 供应商ID
procurementSupplierId = sempo['供应商ID']
# 采购单订单类型
orderType = sempo['采购单类型']

# 供应商
supplier = SupplierMent().supplierparams()
print(supplier)
# 第一笔付款比例
payOne = supplier['第一笔付款比例']
# 第二笔付款比例
payTwo = supplier['第二笔付款比例']
# 第三笔付款比例
payThree = supplier['第三笔付款比例']
# 限制金额
limitAmount = supplier['限制金额']
# 是否票到付尾款   True: 是  False: 否
finalPaymentOnDelivery = supplier['是否票到付尾款']
# 付款方式
paymentType = supplier['付款方式']

# 判断供应商付款方式
if paymentType == 1:
    # 判断该采购单该生成的付款单类型以及数量
    if tax == 0:  # 不含税
        # 样品单与配件单
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

    elif tax == 1:  # 含税
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
                    else:  # 大于等于限制金额
                        # 第一笔第二笔合成一笔无票可付  第三笔生成票到付款
                        if noTicketToPay == 1 and ticketToPayment == 1:
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
else:
    print('供应商为应付款')
