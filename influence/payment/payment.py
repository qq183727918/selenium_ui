# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/17 14:17
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : payment.py
# @Software : PyCharm
import requests
import pprint
from params.sem_params import ParamsTest


class PayMent:

    def paymentest(self):
        token = ParamsTest().token()
        purchaseSn = ParamsTest().purchaseorder()
        url = "https://gateway.test.vevor.net/scp-procurement-service/controller-procurementPaymentOpsService/front/getList"

        querystring = {
            "status": "",
            "paymentMethod": "",
            "attribute": "",
            "purchaseSn": purchaseSn,
            "PurchaseStatus": "",
            "PurchaseType": "",
            "groupId": "",
            "tax": "",
            "consignee": "",
            "refundStatus": "",
            "receiptStatus": "",
            "supplierId": "",
            "badPaypal": "",
            "type": 0,
            "currentPage": 1,
            "pageSize": 10
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": token
        }

        response = requests.get(url, headers=headers, params=querystring)

        re = response.json()

        # pprint.pprint(re)

        data = re["data"]
        noTicketToPay = 0
        ticketToPayment = 0
        for i in data:
            if i["attributeName"] == "无票可付":
                noTicketToPay += 1
            elif i["attributeName"] == "票到付款":
                ticketToPayment += 1
            else:
                print('该属性错误')
        print(f"无票可付:{noTicketToPay}", f"票到付款:{ticketToPayment}")

        return noTicketToPay, ticketToPayment


if __name__ == '__main__':
    pm = PayMent()
    pm.paymentest()
