# _*_ coding: UTF-8 _*_
# @Time     : 2021/1/13 8:46
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : pytest_test_2.py
# @Software : PyCharm

import pytest


class Test1:

    def explanation(self):
        """
        先执行2，  测试用例1依赖测试用例2
        """

    @pytest.mark.dependency(depends=['b'])
    def test_1(self):
        assert True

    # @pytest.mark.run(order=0)
    @pytest.mark.dependency(name="b")
    def test_2(self):
        assert True


if __name__ == '__main__':
    pytest.main(["-v", "-s", "pytest_test_2.py"])
