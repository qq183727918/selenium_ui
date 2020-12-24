# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/17 22:38
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : SupplierManagement.py
# @Software : PyCharm

import requests
import pprint
from params.sem_params import ParamsTest
from influence.purchaseOrder.purchaseorder import PurchaseOrderParams
from file_pre.read_token import ReadToken
from influence.judgingThatTheTokenIsInvalid.judgingThatTheTokenIsInvalid import InviTation


class SupplierMent:
    def supplierparams(self):
        token = ReadToken().retoken()
        dicts = PurchaseOrderParams().params()
        urla = ParamsTest().url_pre()
        procurementSupplierId = dicts["供应商ID"]
        print(procurementSupplierId)

        url = f'{urla}scp-procurement-service/controller-supplierService/front/getSupplierDetail'
        querystring = {
            "supplierId": procurementSupplierId
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f'Bearer {token}'
        }
        respon = requests.get(url, headers=headers, params=querystring)

        re = respon.json()

        # pprint.pprint(re)

        TheTokenValue = InviTation().token_code(re['code'])

        if TheTokenValue == 200:
            dictsa = {
                # 第一笔付款比例
                '第一笔付款比例': re['data']['payOne'],
                # 第二笔付款比例
                '第二笔付款比例': re['data']['payTwo'],
                # 第三笔付款比例
                '第三笔付款比例': re['data']['payThree'],
                # 是否票到付尾款
                '是否票到付尾款': re['data']["isArrivalPay"],
                # 限制金额
                '限制金额': re['data']["limitAmount"],
                # 付款方式
                '付款方式': re['data']['paymentType']
            }

            # pprint.pprint(dictsa)

            return dictsa
        elif TheTokenValue == 401:
            self.supplierparams()
        elif TheTokenValue == '请找相关开发人员解决':
            print('请找相关开发人员解决')
        else:
            print('请检查代码逻辑，谢谢')


if __name__ == '__main__':
    sem = SupplierMent()
    sem.supplierparams()
