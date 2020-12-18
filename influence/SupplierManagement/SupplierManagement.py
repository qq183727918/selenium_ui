# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/17 22:38
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : SupplierManagement.py
# @Software : PyCharm
import requests
import pprint
from params.sem_params import ParamsTest

token = ParamsTest().token()
purchaseSn = ParamsTest().purchaseorder()
url = 'https://gateway.test.vevor.net/scp-procurement-service/controller-supplierService/front/getSupplierDetail?supplierId=3072'
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": token
}
respon = requests.get(url, headers=headers)

re = respon.json()

pprint.pprint(re)
data = re['payOne']
data1 = re['payThree']
data2 = re['payTwo']

