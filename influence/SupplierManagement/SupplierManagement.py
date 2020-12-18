# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/17 22:38
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : SupplierManagement.py
# @Software : PyCharm
import requests
import pprint
from params.sem_params import ParamsTest
from influence.purchaseOrder.purchaseorder import PurchaseOrderParams


class SupplierMent:
    def supplierparams(self):
        token = ParamsTest().token()
        dicts = PurchaseOrderParams().params()
        procurementSupplierId = dicts["procurementSupplierId"]
        url = 'https://gateway.test.vevor.net/scp-procurement-service/controller-supplierService/front/getSupplierDetail'
        params = {
            "supplierId": procurementSupplierId
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": token
        }
        respon = requests.get(url, headers=headers, json=params)

        re = respon.json()

        pprint.pprint(re)

        dictsa = {
            # 第一笔付款比例
            'payOne': re['payOne'],
            # 第二笔付款比例
            'payTwo': re['payTwo'],
            # 第三笔付款比例
            'payThree': re['payThree'],
            # 是否票到付尾款
            'isArrivalPay': re["isArrivalPay"],
            # 限制金额
            'limitAmount': re["limitAmount"]
        }

        return dictsa


if __name__ == '__main__':
    sem = SupplierMent()
    sem.supplierparams()
