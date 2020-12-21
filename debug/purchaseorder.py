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

    payload = [{
        "billSource": 1,
        "dateSource": 2,
        "goodsId": 406,
        "id": 7,
        "orderType": a,
        "procurementSupplierName": "上海中宝不锈钢制品有限公司",
        "productCategory": 7,
        "productName": "liuxiaoqiang 黑色10L",
        "purchaseNumber": 100,
        "purchasePrice": 1000,
        "skuName": "liuxiaoqiang 黑色10L",
        "skuOm": "HSBDDWCTLIUXIESNGV0","tax": 1}]

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer d29a30bb-a3ef-4b5c-87ce-3d58e00ee8bc"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)
