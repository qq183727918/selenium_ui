# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/17 14:50
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : sem_login.py
# @Software : PyCharm
import requests
from params.sem_params import ParamsTest


class SemLoginTest:
    def semtoken(self):
        querystring = {
            "username": "liuxiaoqiang",
            "password": "c90a3167151be42f910045215f6aac96",
            "grant_type": "password"
        }

        self.urla = ParamsTest().urls()

        url = f"{self.urla}/controller-authLoginController/login?username=liuxiaoqiang&password=c90a3167151be42f910045215f6aac96&grant_type=password"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic YXV0aDoxMjM=",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
        }

        response = requests.post(url, headers=headers, params=querystring)

        re = response.json()

        token = re["data"]["access_token"]

        print(token)

        return token


if __name__ == '__main__':
    sem = SemLoginTest()
    sem.semtoken()
