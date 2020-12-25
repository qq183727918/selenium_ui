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
            'billSource': 1,
            'dateSource': 2,
            'goodsId': 4,
            'id': 4,
            'orderType': 5,
            'procurementSupplierName': "文登奥文电机有限公司",
            'productCategory': 4,
            'productName': '砂光机-12"圆盘砂光机V2',
            'purchaseNumber': 1000,
            'purchasePrice': 572.73,
            'skuName': '砂光机-12"圆盘砂光机V2',
            'skuOm': "YPSGJ-12V29H9K1KKV2",
            'tax': 1
        }]

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer f3e7a10b-c4bf-445c-bb21-c81eedd09222"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)


fff()
