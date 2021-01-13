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
        测试用例1依赖测试用例2
        只有test_2成功test_1才会执行，否则test_1跳过
        """
    @pytest.mark.run(order=1)
    @pytest.mark.dependency(depends=['b'])
    def test_1(self):
        print('test_2不通过，该条不执行')
        # assert True

    @pytest.mark.run(order=0)
    @pytest.mark.dependency(name="b")
    def test_2(self):
        print('该条通过，test_1才能执行')
        # assert True


if __name__ == '__main__':
    pytest.main(["-v", "-s", "pytest_test_2.py"])
