# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/23 9:18
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : pre.py
# @Software : PyCharm

import requests

url = "https://gatewaypreprod.vevor.net/scp-procurement-service/controller-purchaseOrderService/front/addPurchaseOrder"

payload = [
    {
        "billSource": 1,
        "dateSource": 2,
        "goodsId": 2,
        "id": 2,
        "orderType": 2,
        "procurementSupplierName": "文登奥文电机有限公司",
        "productCategory": 279,
        "productName": '砂光机-6"砂盘2 * 42砂带机V1',
        "purchaseNumber": 1,
        "purchasePrice": 536.36,
        "replaceGoodsId": "",
        "skuName": '砂光机-6"砂盘2 * 42砂带机V1',
        "skuOm": "GPSDJ-6242V1JSNPKV1",
        "tax": 1
    }]

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer aeeee8e5-e3d6-47ed-b028-676405be39dd"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)

