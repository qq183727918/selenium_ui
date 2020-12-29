# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/25 0:16
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : payment.py
# @Software : PyCharm
import requests
from influence.judgingThatTheTokenIsInvalid.judgingThatTheTokenIsInvalid import InviTation
from params.sem_params import ParamsTest
from file_pre.read_token import ReadToken


class PayMent:

    def paymentest(self, purchaseSn):
        self.urla = ParamsTest().selenium_url_pre()
        token = ReadToken().retoken()
        url = f"{self.urla}scp-procurement-service/controller-procurementPaymentOpsService/front/getList"

        querystring = {
            "status": "",
            "paymentMethod": "",
            "attribute": "",
            "purchaseSn": purchaseSn,
            "PurchaseStatus": "",
            "PurchaseType": "",
            "groupId": "",
            "tax": "",
            "consignee": "",
            "refundStatus": "",
            "receiptStatus": "",
            "supplierId": "",
            "badPaypal": "",
            "type": 0,
            "currentPage": 1,
            "pageSize": 10
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f'Bearer {token}'
        }

        response = requests.get(url, headers=headers, params=querystring)

        re = response.json()

        TheTokenValue = InviTation().token_code(re['code'])

        if TheTokenValue == 200:

            # pprint.pprint(re)

            data = re["data"]
            lists = []
            for k in data:
                dict = {
                    # "paymenttype": "预付款单",
                    "paymentAmount": "",
                    "attributeName": ""
                }
                # 付款单金额
                paymentAmount = k["paymentAmount"]
                # 付款单属性（无票可付、票到付款）
                attributeName = k["attributeName"]
                dict["paymentAmount"] = paymentAmount
                dict["attributeName"] = attributeName
                lists.append(dict)

            print(lists)

            return lists
        elif TheTokenValue == 401:
            self.paymentest(purchaseSn)
        elif TheTokenValue == '请找相关开发人员解决':
            print('请找相关开发人员解决')
        else:
            print('请检查代码逻辑，谢谢')


if __name__ == '__main__':
    purchaseSn = 'NCG2020122400034'
    pm = PayMent()
    pm.paymentest(purchaseSn)
