# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/23 14:38
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : 123.py
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
            'goodsId': 411,
            'id': 12,
            'orderType': a,
            'procurementSupplierName': "深圳市凯信达能源技术有限公司",
            'productCategory': 12,
            'productName': "das 黑色",
            'purchaseNumber': 100,
            'purchasePrice': 1000,
            'skuName': "das 黑色",
            'skuOm': "HSBDDWCTDASQGU0D1V0",
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
