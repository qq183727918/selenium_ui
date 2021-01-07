# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/24 21:46
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : flask_test.py
# @Software : PyCharm

from debug.procur.payment import PayMent
from debug.procur.procurchase import PurchaseOrderParams
from debug.procur.supplier import SupplierMent
from flask import Flask
import flask
import json

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    # from-data格式参数
    global ren
    purchaseSn = flask.request.values.get('purchaseSn')
    print(purchaseSn)
    # 付款单
    sempayment = PayMent()
    semp = sempayment.paymentest(purchaseSn)
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
    sempo = sempurchaseorder.params(purchaseSn)
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
    supplier = SupplierMent().supplierparams(purchaseSn)
    print(supplier)
    # 第一笔付款比例
    payOne = supplier['第一笔付款比例']
    payOnepirc = pirc * payOne * 0.01
    # 第二笔付款比例
    payTwo = supplier['第二笔付款比例']
    payTwopirc = pirc * payTwo * 0.01
    # 第三笔付款比例
    payThree = supplier['第三笔付款比例']
    payThreepirc = pirc * payThree * 0.01
    # 限制金额
    limitAmount = supplier['限制金额']
    # 是否票到付尾款   True: 是  False: 否
    finalPaymentOnDelivery = supplier['是否票到付尾款']
    # 付款方式
    paymentType = supplier['付款方式']
    print('=========================================================================]')

    print(semp[0]['paymentAmount'], semp[1]['paymentAmount'], semp[2]['paymentAmount'])
    print(payOnepirc, payTwopirc, payThreepirc)

    # 判断供应商付款方式
    if paymentType == 1:
        # 判断该采购单该生成的付款单类型以及数量
        if tax == 0:  # 不含税
            # 样品单与配件单
            if orderType == 0 or orderType == 3:
                # 一笔无票可付
                if noTicketToPay == 1 and ticketToPayment == 0:
                    if semp[0]['paymentAmount'] == pirc:
                        ren = {'msg_code': 139500, 'msg': '采购单生成付款单正确', 'data': semp}
                        print('采购单生成付款单正确')
                    else:
                        ren = {'msg_code': 139501, 'msg': '采购单生成付款单不正确', 'data': semp}
                        print('采购单生成付款单不正确，金额错误')
                elif noTicketToPay == 0 and ticketToPayment == 0:
                    ren = {'msg_code': 139510, 'msg': '采购单生成未生成付款单', 'data': semp}
                    print('采购单生成未生成付款单')
                else:
                    ren = {'msg': '采购单生成的付款单不正确', 'msg_code': 139504, 'data': 'null'}
                    print('采购单生成的付款单不正确')
            else:
                if pirc > 5000:
                    # 第一笔第二笔合成一笔无票可付，第三笔无票可付
                    if noTicketToPay == 2 and ticketToPayment == 0:
                        if (payTwopirc + payTwopirc == sempo[0]['paymentAmount']) and (payThreepirc == sempo[1]['paymentAmount']):
                            ren = {'msg_code': 139500, 'msg': '采购单生成付款单正确', 'data': semp}
                            print('采购单生成付款单正确')
                        else:
                            ren = {'msg_code': 139501, 'msg': '采购单生成付款单不正确', 'data': semp}
                            print('采购单生成付款单不正确，金额错误')
                    elif noTicketToPay == 0 and ticketToPayment == 0:
                        ren = {'msg_code': 139510, 'msg': '采购单生成未生成付款单', 'data': semp}
                        print('采购单生成未生成付款单')
                    else:
                        ren = {'msg': '采购单生成的付款单不正确', 'msg_code': 139504, 'data': 'null'}
                        print('采购单生成的付款单不正确')
                elif pirc <= 5000:
                    # 一笔无票可付
                    if noTicketToPay == 1 and ticketToPayment == 0:
                        if semp[0]['paymentAmount'] == pirc:
                            ren = {'msg_code': 139500, 'msg': '采购单生成付款单正确', 'data': semp}
                            print('采购单生成付款单正确')
                        else:
                            ren = {'msg_code': 139501, 'msg': '采购单生成付款单不正确', 'data': semp}
                            print('采购单生成付款单不正确，金额错误')
                    elif noTicketToPay == 0 and ticketToPayment == 0:
                        ren = {'msg_code': 139510, 'msg': '采购单生成未生成付款单', 'data': semp}
                        print('采购单生成未生成付款单')
                    else:
                        ren = {'msg': '采购单生成的付款单不正确', 'msg_code': 139504, 'data': 'null'}
                        print('采购单生成的付款单不正确')

        elif tax == 1:  # 含税
            # 配件单与样品单
            if orderType == 0 or orderType == 3:
                # 一笔无票可付
                if noTicketToPay == 1 and ticketToPayment == 0:
                    if semp[0]['paymentAmount'] == pirc:
                        ren = {'msg_code': 139500, 'msg': '采购单生成付款单正确', 'data': semp}
                        print('采购单生成付款单正确')
                    else:
                        ren = {'msg_code': 139501, 'msg': '采购单生成付款单不正确', 'data': semp}
                        print('采购单生成付款单不正确，金额错误')
                elif noTicketToPay == 0 and ticketToPayment == 0:
                    ren = {'msg_code': 139510, 'msg': '采购单生成未生成付款单', 'data': semp}
                    print('采购单生成未生成付款单')
                else:
                    ren = {'msg': '采购单生成的付款单不正确', 'msg_code': 139504, 'data': 'null'}
                    print('采购单生成的付款单不正确')
            else:
                if pirc >= 5000:
                    # 判断是否票到付尾款
                    if finalPaymentOnDelivery:  # 0是，票到付尾款
                        # 一笔无票可付，第两笔第三笔票到付款
                        if noTicketToPay == 1 and ticketToPayment == 2:
                            if semp[0]['paymentAmount'] == payOnepirc and semp[1]['paymentAmount'] == payTwopirc and semp[2]['paymentAmount'] == payThreepirc:
                                ren = {'msg_code': 139500, 'msg': '采购单生成付款单正确', 'data': semp}
                                print('采购单生成付款单正确')
                            else:
                                ren = {'msg_code': 139501, 'msg': '采购单生成付款单不正确', 'data': semp}
                                print('采购单生成付款单不正确，金额错误')
                        else:
                            ren = {'msg': '采购单生成的付款单不正确', 'msg_code': 139504, 'data': 'null'}
                            print('采购单生成的付款单不正确')
                    elif not finalPaymentOnDelivery:  # 1否，票到付尾款
                        if pirc < limitAmount:  # 小于限制金额
                            # 一笔无票可付
                            if noTicketToPay == 1 and ticketToPayment == 0:
                                if semp[0]['paymentAmount'] == pirc:
                                    ren = {'msg_code': 139500, 'msg': '采购单生成付款单正确', 'data': semp}
                                    print('采购单生成付款单正确')
                                else:
                                    ren = {'msg_code': 139501, 'msg': '采购单生成付款单不正确', 'data': semp}
                                    print('采购单生成付款单不正确，金额错误')
                            elif noTicketToPay == 0 and ticketToPayment == 0:
                                ren = {'msg_code': 139510, 'msg': '采购单生成未生成付款单', 'data': semp}
                                print('采购单生成未生成付款单')
                            else:
                                ren = {'msg': '采购单生成的付款单不正确', 'msg_code': 139504, 'data': 'null'}
                                print('采购单生成的付款单不正确')
                        else:  # 大于等于限制金额
                            # 第一笔第二笔合成一笔无票可付  第三笔生成票到付款
                            if noTicketToPay == 1 and ticketToPayment == 1:
                                if (payTwopirc + payTwopirc == semp[0]['paymentAmount']) and (payThreepirc == semp[1]['paymentAmount']):
                                    ren = {'msg_code': 139500, 'msg': '采购单生成付款单正确', 'data': semp}
                                    print('采购单生成付款单正确')
                                else:
                                    ren = {'msg_code': 139501, 'msg': '采购单生成付款单不正确', 'data': semp}
                                    print('采购单生成付款单不正确，金额错误')
                            elif noTicketToPay == 0 and ticketToPayment == 0:
                                ren = {'msg_code': 139510, 'msg': '采购单生成未生成付款单', 'data': semp}
                                print('采购单生成未生成付款单')
                            else:
                                ren = {'msg': '采购单生成的付款单不正确', 'msg_code': 139504, 'data': 'null'}
                                print('采购单生成的付款单不正确')
                    else:
                        ren = {'msg': '采购单生成的付款单不正确', 'msg_code': 139504, 'data': 'null'}
                        print('采购单生成的付款单不正确')
                elif pirc < 5000:
                    # 一笔无票可付
                    if noTicketToPay == 1 and ticketToPayment == 0:
                        if semp[0]['paymentAmount'] == pirc:
                            ren = {'msg_code': 139500, 'msg': '采购单生成付款单正确', 'data': semp}
                            print('采购单生成付款单正确')
                        else:
                            ren = {'msg_code': 139501, 'msg': '采购单生成付款单不正确', 'data': semp}
                            print('采购单生成付款单不正确，金额错误')
                    elif noTicketToPay == 0 and ticketToPayment == 0:
                        ren = {'msg_code': 139510, 'msg': '采购单生成未生成付款单', 'data': semp}
                        print('采购单生成未生成付款单')
                    else:
                        ren = {'msg': '采购单生成的付款单不正确', 'msg_code': 139504, 'data': 'null'}
                        print('采购单生成的付款单不正确')
                else:
                    ren = {'msg': '采购价错误', 'msg_code': 139503, 'data': 'null'}
                    print('采购价错误')
        else:
            ren = {'msg': '是否含税类型错误', 'msg_code': 139502, 'data': 'null'}
            print('是否含税类型错误')
    else:
        ren = {'msg': '供应商为应付款', 'msg_code': 139501, 'data': 'null'}
        print('供应商为应付款')

    return json.dumps(ren, ensure_ascii=False)


if __name__ == '__main__':
    app.run(port=80, debug=True, host='0.0.0.0')  # 启动服务
    # debug=True,改了代码后，不用重启，它会自动重启
    # 'host='127.0.0.1'别IP访问地址
