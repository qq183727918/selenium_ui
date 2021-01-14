# _*_ coding: UTF-8 _*_
# @Time     : 2021/1/13 8:52
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : pytest_test_3.py
# @Software : PyCharm
import pytest


@pytest.mark.run(order=-5)
@pytest.mark.dependency(depends=["pytest_test_4.py::test_a"], scope='session')
def test_b():
    a = 1
    assert a == 1





