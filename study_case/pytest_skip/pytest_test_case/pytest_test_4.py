# _*_ coding: UTF-8 _*_
# @Time     : 2021/1/13 8:53
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : pytest_test_4.py
# @Software : PyCharm

import pytest


@pytest.mark.run(order=-10)
@pytest.mark.dependency()
def test_a():
    a = 1
    assert a == 1
