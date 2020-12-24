# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/16 19:09
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : purchaseorder.py
# @Software : PyCharm
import requests
from params.sem_params import ParamsTest
from file_pre.read_token import ReadToken
from influence.judgingThatTheTokenIsInvalid.judgingThatTheTokenIsInvalid import InviTation


class PurchaseOrderParams:

    def __init__(self):
        self.pirc = ''
        self.tax = ''
        self.procurementSupplierId = ''
        self.orderType = ''

    def orderparams(self):
        token = ReadToken().retoken()
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
        self.urla = ParamsTest().url_pre()

        url = f"{self.urla}scp-procurement-service/controller-purchaseOrderService/front/getPurchaseOrderList"

        headers = {
            "Content-Type": "application/json",
            "Authorization": f'Bearer {token}'
        }

        response = requests.get(url, headers=headers, params=querystring)

        re = response.json()

        TheTokenValue = InviTation().token_code(re['code'])

        if TheTokenValue == 200:
            # import pprint
            # pprint.pprint(re)
            try:
                # 采购总价
                self.pirc = re["data"]["list"][0]["purchasePriceAll"]
                # print(f'采购总价:{self.pirc}')
                # 是否含税
                self.tax = re["data"]["list"][0]["tax"]
                # print(f'是否含税:{self.tax}')
                # 供应商ID
                self.procurementSupplierId = re["data"]["list"][0]["procurementSupplierId"]
                # print(f'供应商ID:{self.procurementSupplierId}')
                # 采购单类型
                self.orderType = re["data"]["list"][0]["orderType"]
                # print(f'采购单类型:{self.orderType}')

            except Exception as e:
                print(e)
        elif TheTokenValue == 401:
            self.orderparams()
        elif TheTokenValue == '请找相关开发人员解决':
            print('请找相关开发人员解决')
        else:
            print('请检查代码逻辑，谢谢')

    def params(self):
        self.orderparams()
        dicts = {"采购总价": self.pirc,
                 "是否含税": self.tax,
                 "供应商ID": self.procurementSupplierId,
                 "采购单类型": self.orderType}
        return dicts


if __name__ == '__main__':
    pop = PurchaseOrderParams()
    pop.params()
