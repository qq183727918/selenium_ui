# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/10 10:58
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : params.py
# @Software : PyCharm

class ParamsTest:

    def movemoney(self):
        """移款单号"""
        movemoney = ''
        return movemoney

    def payment(self):
        """付款单号"""
        payment = ''
        return payment

    def transit(self):
        """在途单"""
        transit = ''
        return transit

    def purchaseorder(self):
        """采购单"""
        purchaseorder = 'NCG2020122300452'
        return purchaseorder

    def warehousereceipt(self):
        """入库单"""
        warehousereceipt = 'DH202007240002'
        return warehousereceipt

    def upshelforder(self):
        """上架单"""
        upshelforder = ''
        return upshelforder

    def returnshelforder(self):
        """返架单"""
        returnshelforder = ''
        return returnshelforder

    def latestoverseas(self):
        """海外仓"""
        latestoverseas = ''
        return latestoverseas

    def token(self):
        """token"""
        from influence.sem_login.sem_login import SemLoginTest
        tokens = SemLoginTest()
        tokena = tokens.semtoken()
        tokens = f'Bearer {tokena}'
        return tokens

    def urls(self):
        """请求头"""
        url = 'https://gatewaypre.vevor.net/scp-procurement-service'

        return url

    def url_test(self):
        """selenium url"""
        url_test = 'http://sem.test.vevor.net/'
        return url_test

    def url_pre(self):
        """selenium url"""
        url_pre = 'http://sem.pre.vevor.net/'
        return url_pre
