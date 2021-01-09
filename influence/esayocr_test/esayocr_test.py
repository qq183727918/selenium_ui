# _*_ coding: UTF-8 _*_
# @Time     : 2021/1/9 14:25
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : esayocr_test.py
# @Software : PyCharm

import easyocr

reader = easyocr.Reader(['ch_sim', 'en'])

GPU = False

result = reader.readtext('./123.png')

print(result)

