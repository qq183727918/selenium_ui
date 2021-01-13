# _*_ coding: UTF-8 _*_
# @Time     : 2021/1/13 8:41
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : pytest_order_test.py
# @Software : PyCharm

import pytest


class Test1:

    def explanation(self):

        """
        按照指定顺序执行测试用例
        """

    @pytest.mark.run(order=5)
    def test_1(self):
        pass

    @pytest.mark.run(order=0)
    def test_2(self):
        pass

    @pytest.mark.run(order=1)
    def test_3(self):
        pass

    @pytest.mark.run(order=-1)
    def test_4(self):
        pass

    @pytest.mark.run(order=-5)
    def test_5(self):
        pass

    def test_6(self):
        pass


if __name__ == '__main__':
    pytest.main(["-v", "-s", "pytest_order_test.py"])
