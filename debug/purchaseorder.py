# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/21 17:45
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : purchaseorder.py
# @Software : PyCharm
import requests

i = 0
while True:
    i += 1
    print(f'第{i}循环')
    if i % 2 == 0:
        a = 5
    else:
        a = 4
    url = "https://gatewaypre.vevor.net/scp-procurement-service/controller-purchaseOrderService/front/addPurchaseOrder"

    payload = [
        {
            'billSource': 1,
            'dateSource': 2,
            'goodsId': 410,
            'id': 11,
            'orderType': a,
            'procurementSupplierName': "中山市修本照明有限公司",
            'productCategory': 11,
            'productName': "童俊SPU 黑色10L170",
            'purchaseNumber': 100,
            'purchasePrice': 1000,
            'skuName': "童俊SPU 黑色10L170",
            'skuOm': "TJHSSDYMCSPU13SPDV5"
        },
        {
            'billSource': 1,
            'dateSource': 2,
            'goodsId': 409,
            'id': 10,
            'orderType': a,
            'procurementSupplierName': "中山市修本照明有限公司",
            'productCategory': 10,
            'productName': "童俊SPU 黑色10L170",
            'purchaseNumber': 100,
            'purchasePrice': 1000,
            'skuName': "童俊SPU 黑色10L170",
            'skuOm': "TJHSOCSPU10L1GI6FV2",
            'tax': 1
        },
        {
            'billSource': 1,
            'dateSource': 2,
            'goodsId': 406,
            'id': 7,
            'orderType': a,
            'procurementSupplierName': "中山市修本照明有限公司",
            'productCategory': 7,
            'productName': "liuxiaoqiang 黑色10L",
            'purchaseNumber': 100,
            'purchasePrice': 1000,
            'skuName': "liuxiaoqiang 黑色10L",
            'skuOm': "HSBDDWCTLIUXIESNGV0",
            'tax': 1
        }]

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 954c0491-91e3-40da-a097-b5f4a3ad1509"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)
    if i == 50:
        break
