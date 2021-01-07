# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/23 14:38
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : 123.py
# @Software : PyCharm
import requests
import pprint
from influence.sem_login.sem_login import SemLoginTest
from file_pre.read_token import ReadToken
from influence.judgingThatTheTokenIsInvalid.judgingThatTheTokenIsInvalid import InviTation


def postpurchase():
    token = ReadToken().retoken()
    url = "https://gatewaypreprod.vevor.net/scp-procurement-service/controller-purchaseOrderService/front/addPurchaseOrder"

    payload = [
    {
        "billSource": 0,
        "dateSource": 2,
        "goodsId": 16,
        "id": 16,
        "orderType": 2,
        "procurementSupplierName": "靖江联新机械配件有限公司",
        "productCategory": 279,
        "productName": "推车1000磅49*24.5",
        "purchaseNumber": 1000,
        "purchasePrice": 236.36,
        "skuName": "推车1000磅49*24.5",
        "skuOm": "TC1000B4924.50001V0",
        "tax": 1
    },
    {
        "billSource": 0,
        "dateSource": 2,
        "goodsId": 17,
        "id": 17,
        "orderType": 2,
        "procurementSupplierName": "靖江联新机械配件有限公司",
        "productCategory": 279,
        "productName": "推车(1200磅47.5*22.5",
        "purchaseNumber": 1000,
        "purchasePrice": 290.91,
        "skuName": "推车(1200磅47.5*22.5",
        "skuOm": "TC1200B47.522.501V0",
        "tax": 1
    }
]
    headers = {
        "Content-Type": "application/json",
        # 请求token
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(url, json=payload, headers=headers)

    re = response.json()

    # pprint.pprint(re)

    TheTokenValue = InviTation().token_code(re['code'])

    if TheTokenValue == 200:

        pprint.pprint(re)

    elif TheTokenValue == 401:
        postpurchase()
    elif TheTokenValue == '请找相关开发人员解决':
        print('请找相关开发人员解决')
    else:
        print('请检查代码逻辑，谢谢')


postpurchase()
