# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/18 14:35
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : purchaseinfluence.py
# @Software : PyCharm
import requests
from params.sem_params import ParamsTest

urla = ParamsTest().request_url_pre()
url = f"{urla}/controller-purchaseOrderService/front/addPurchaseOrder"

payload = [{
    "billSource": 1,
    "dateSource": 2,
    "goodsId": 404,
    "id": 7,
    "orderType": 4,
    "procurementSupplierName": "深圳市凯信达能源技术有限公司",
    "productCategory": 7,
    "productName": "liuxiaoqiang 黑色10L",
    "purchaseNumber": 100,
    "purchasePrice": 1000,
    "skuName": "liuxiaoqiang 黑色10L",
    "skuOm": "HSBDDWCTLIUXIESNGV0",
    "tax": 1
}]

headers = {
    "Authorization": "Bearer 1b60d12f-ef00-4fb5-8745-2adc5a057a3b",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

re = response.json()

import pprint

pprint.pprint(re)
