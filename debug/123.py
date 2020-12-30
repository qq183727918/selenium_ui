# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/23 14:38
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : 123.py
# @Software : PyCharm
import pytesseract
import requests

i = 0


def fff():
    url = "https://gatewaypre.vevor.net/scp-procurement-service/controller-purchaseOrderService/front/addPurchaseOrder"

    payload = [
        {
            'billSource': 0,
            'dateSource': 2,
            'goodsId': 4,
            'id': 4,
            'orderType': 5,
            'procurementSupplierName': "文登奥文电机有限公司",
            'productCategory': 279,
            'productName': '砂光机-12"圆盘砂光机V2',
            'purchaseNumber': 100,
            'purchasePrice': 572.73,
            'skuName': '砂光机-12"圆盘砂光机V2',
            'skuOm': "YPSGJ-12V29H9K1KKV2",
            'tax': 1
        }]

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 73fb0c64-c5de-4f0e-a060-032d28cdaecc"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)


fff()
