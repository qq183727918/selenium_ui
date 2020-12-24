# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/24 10:29
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : judgingThatTheTokenIsInvalid.py
# @Software : PyCharm
from influence.sem_login.sem_login import SemLoginTest


class InviTation:

    def token_code(self, re):
        if re == 200:
            print('token可以正常使用，请继续')
            return 200
        elif re == 401:
            print('token失效，正在重新获取token')
            sem = SemLoginTest()
            sem.semtoken()
            print('获取token成功，正在重试，请稍等......')
            return 401
        elif re == 503 or 500:
            print('请找相关开发人员解决')
            develop = '请找相关开发人员解决'
            return develop
        else:
            print('响应码为识别')


if __name__ == '__main__':
    re = 401
    code = InviTation()
    code.token_code(re)
