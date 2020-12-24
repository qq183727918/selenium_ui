# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/17 14:17
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : payment.py
# @Software : PyCharm
import requests
from params.sem_params import ParamsTest
from params.sem_params import ParamsTest

class PayMent:

    def paymentest(self):
        self.urla = ParamsTest().urls()
        token = ParamsTest().token()
        purchaseSn = ParamsTest().purchaseorder()
        url = f"{self.urla}/controller-procurementPaymentOpsService/front/getList"

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
        lists = []
        for k in data:
            dict = {
                "paymentAmount": "",
                "attributeName": ""
            }
            # 付款单金额
            paymentAmount = k["paymentAmount"]
            # 付款单属性（无票可付、票到付款）
            attributeName = k["attributeName"]
            dict["paymentAmount"] = paymentAmount
            dict["attributeName"] = attributeName
            lists.append(dict)

        return lists


if __name__ == '__main__':
    pm = PayMent()
    pm.paymentest()
