# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/16 19:09
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : purchaseorder.py
# @Software : PyCharm
import requests
from params.sem_params import ParamsTest


class PurchaseOrderParams:

    def __init__(self):
        self.pirc = ''
        self.tax = ''
        self.procurementSupplierId = ''
        self.orderType = ''

    def orderparams(self):
        token = ParamsTest().token()
        purchaseSn = ParamsTest().purchaseorder()
        querystring = {
            "currentPage": "1",
            "pageSize": "10",
            "purchaseStatus": "",
            "orderType": "",
            "billSource": "",
            "freeze": "",
            "procurementSupplierId": "",
            "groupId": "",
            "purchaseSn": purchaseSn
        }

        url = "https://gateway.test.vevor.net/scp-procurement-service/controller-purchaseOrderService/front/getPurchaseOrderList"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": token
        }

        response = requests.get(url, headers=headers, params=querystring)

        re = response.json()
        import pprint
        # pprint.pprint(re)
        # 采购总价
        self.pirc = re["data"]["list"][0]["purchasePriceAll"]
        # 是否含税
        self.tax = re["data"]["list"][0]["tax"]
        # 供应商ID
        self.procurementSupplierId = re["data"]["list"][0]["procurementSupplierId"]
        # 采购单类型
        self.orderType = re["data"]["list"][0]["orderType"]
        # print(self.pirc)

    def params(self):
        self.orderparams()
        dicts = {"pirc": self.pirc,
                 "tax": self.tax,
                 "procurementSupplierId": self.procurementSupplierId,
                 "orderType": self.orderType}
        return dicts


if __name__ == '__main__':
    pop = PurchaseOrderParams()
    pop.orderparams()
