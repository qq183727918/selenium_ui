# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/17 14:50
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : sem_login.py
# @Software : PyCharm
import requests


class SemLoginTest:
    def semtoken(self):
        querystring = {
            "username": "liuxiaoqiang",
            "password": "c90a3167151be42f910045215f6aac96",
            "grant_type": "password"
        }

        url = "https://gateway.test.vevor.net/center-user-service/controller-authLoginController/login"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic YXV0aDoxMjM="
        }

        response = requests.post(url, headers=headers, params=querystring)

        re = response.json()

        token = re["data"]["access_token"]

        # print(token)

        return token


if __name__ == '__main__':
    sem = SemLoginTest()
    sem.semtoken()
