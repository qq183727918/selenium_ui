# _*_ coding: UTF-8 _*_
# @Time     : 2021/1/13 15:05
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : pytest_test_5.py
# @Software : PyCharm

import pytest


@pytest.mark.run(order=5)
@pytest.mark.dependency(depends=["test_cart"])
def test_order():
    print("创建订单")


@pytest.mark.run(order=1)
@pytest.mark.dependency()
def test_cart():
    print("添加到购物车")
    a = 0
    assert a == 0



