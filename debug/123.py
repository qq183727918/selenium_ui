# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/23 14:38
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : 123.py
# @Software : PyCharm

import requests

i = 0


def fff():
    url = "https://gatewaypre.vevor.net/scp-procurement-service/controller-purchaseOrderService/front/addPurchaseOrder"

    payload = [
        {
            'billSource': 0,
            'dateSource': 2,
            'goodsId': 11,
            'id': 11,
            'orderType': 4,
            'procurementSupplierName': "枣庄市佳跃机械有限公司",
            'productCategory': 11,
            'productName': '研磨机-750w黑色刀片打磨机V1',
            'purchaseNumber': 1000,
            'purchasePrice': 10000,
            'skuName': '研磨机-750w黑色刀片打磨机V1',
            'skuOm': "YMJ-750WHSDPDMJ01V1",
            'tax': 1
        }]

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 09db02e6-b230-4582-9e09-0b0114fd7f32"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)



fff()



