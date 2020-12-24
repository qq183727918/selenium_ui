# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/24 10:31
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : warehousereceipt.py
# @Software : PyCharm

import pprint
import requests
from file_pre.read_token import ReadToken


class WarehousePre:

    def receipt(self):
        # 查询入库单接口
        url = 'https://gatewaypre.vevor.net/scp-inventory-service/controller-inStockService/inStockPageInfo'
        token = ReadToken().retoken()
        headers = {
            "Content-Type": "application/json",
            "Authorization": f'Bearer {token}'

        }

        params = {
            'concatSn': "NCG2020122300441",
            'createdEndTime': "",
            'createdStartTime': "",
            'currentPage': 1,
            'generateUpShelf': "",
            'groupId': "",
            'inStockSn': "",
            'inStockStatus': "",
            'inStockType': "",
            'pageSize': 10,
            'practicalReceiveEndTime': "",
            'practicalReceiveStartTime': "",
            'predictLoadingEndTime': "",
            'predictLoadingStartTime': "",
            'predictWarehouseEndTime': "",
            'predictWarehouseStartTime': "",
            'seaWarehousesId': "",
            'sku': "",
            'supplierId': ""
        }

        respon = requests.post(url=url, headers=headers, json=params)

        re = respon.json()

        # pprint.pprint(re)

        return re['code']


if __name__ == '__main__':
    sem = WarehousePre()
    sem.receipt()
