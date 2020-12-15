# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/14 19:50
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : purchaseorder.py
# @Software : PyCharm
import requests
import pprint


class PurchaseOrder:

    def order(self):
        url = 'https://gateway.test.vevor.net/scp-procurement-service/controller-purchaseOrderService/front/getPurchaseOrderList'
        querystring = {
            "currentPage": "1",
            "pageSize": "10",
            "purchaseStatus": "",
            "orderType": "",
            "billSource": "",
            "freeze": "",
            "procurementSupplierId": "",
            "groupId": ""}
        payload = ""
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Bearer fe8ade28-eebe-4b8f-a712-a364f4f6f7ca",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
        }

        respon = requests.get(url, data=payload, headers=headers, params=querystring)

        re = respon.json()

        pprint.pprint(re)


if __name__ == '__main__':
    r = PurchaseOrder()
    r.order()
