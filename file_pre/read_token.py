# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/24 10:32
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : read_token.py
# @Software : PyCharm

class ReadToken:
    def retoken(self):
        with open(r'D:\Tools\git\selenium_ui\file_pre\token.txt', 'r')as f:
            token = f.readline()
            # print(token)

        return token


if __name__ == '__main__':
    sem = ReadToken()
    sem.retoken()
