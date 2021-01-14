# _*_ coding: UTF-8 _*_
# @Time     : 2021/1/14 10:15
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : goods_info2.py
# @Software : PyCharm
import requests
from influence.judgingThatTheTokenIsInvalid.judgingThatTheTokenIsInvalid import InviTation
from params.sem_params import ParamsTest
from file_pre.read_token import ReadToken


def goods_info2():
    url = "https://gatewaypreprod.vevor.net/center-goods-service/controller-goodsSupplierService/goodsSupplierInfoAdd"
    token = ReadToken().retoken()
    payload = [{
        "buyingPeopleId": "",
        "buyingPeopleName": "",
        "calculateProdPrice": 12229.47,
        "clearanceId": "",
        "confSupplierId": 0,
        "createdBy": "",
        "createdTime": -30609820800000,
        "deliveryCycle": 42,
        "departurePlace": "靖江",
        "destination": "中国仓：常熟市东张镇富亚路3号",
        "drawbackRate": 0.13,
        "goodsId": 16,
        "id": 9898,
        "invoiceCompany": "",
        "invoiceDot": 0.1,
        "invoiceName": "",
        "invoiceTax": 0.13,
        "isChecked": 1,
        "isDelete": 0,
        "isNew": 0,
        "isReturnSamplePriceDiff": 1,
        "isSampleContainTax": 1,
        "isTaxRefund": 1,
        "key": 9898,
        "minQuantitity": 20,
        "packagePrice": 5,
        "purchaseId": "",
        "shippyFee": 16,
        "supplierLink": "",
        "supplierManagerId": 483,
        "supplierName": "靖江联新机械配件有限公司",
        "supplierStatus": "",
        "taxExclusivePrice": "",
        "taxExclusiveTotalPrice": 12563,
        "taxInclusivePrice": 13819.3,
        "updatedBy": "刘晓强",
        "updatedTime": 1610589440000

    }]

    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}',
        "AuthUserInfo": '{"name":"%E5%88%98%E6%99%93%E5%BC%BA","userId":626,"username":"liuxiaoqiang"}'
    }

    response = requests.post(url=url, json=payload, headers=headers)

    re = response.json()

    TheTokenValue = InviTation().token_code(re['code'])

    if TheTokenValue == 200:
        print(response.text)
    elif TheTokenValue == 401:
        goods_info2()
    elif TheTokenValue == '请找相关开发人员解决':
        print('请找相关开发人员解决')
    else:
        print('请检查代码逻辑，谢谢')


goods_info2()
