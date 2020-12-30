# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/23 14:38
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : 123.py
# @Software : PyCharm
import requests
import pprint

url = "https://gatewaypre.vevor.net/scp-procurement-service/controller-purchaseOrderService/front/addPurchaseOrder"

payload = [
    {
        # 0是系统订单，1是手动创建
        'billSource': 0,
        # 0是ERP数据来源，1是center-goods来源，2是SCP数据来源
        'dateSource': 2,
        # 商品ID
        'goodsId': 4,
        'id': 4,
        # 订单类型，4为额外加货订单，5是FBA订单
        'orderType': 5,
        # 供应商名称
        'procurementSupplierName': "文登奥文电机有限公司",
        'productCategory': 279,
        'productName': '砂光机-12"圆盘砂光机V2',
        # 采购数量
        'purchaseNumber': 100,
        # 采购价格
        'purchasePrice': 572.73,
        'skuName': '砂光机-12"圆盘砂光机V2',
        'skuOm': "YPSGJ-12V29H9K1KKV2",
        # 是否含税
        'tax': 1
    }]

headers = {
    "Content-Type": "application/json",
    # 请求token
    "Authorization": "Bearer 0a4aa5d5-97d0-4175-b160-83582c0bf0af"
}

response = requests.post(url, json=payload, headers=headers)

re = response.json()

pprint.pprint(re)
