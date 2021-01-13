# _*_ coding: UTF-8 _*_
# @Time     : 2021/1/13 8:41
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : pytest_order_test.py
# @Software : PyCharm

import pytest
from study_case.pytest_skip.debug.debug_test_1 import DebugTestOne as do
from study_case.pytest_skip.debug.debug_test_2 import DebugTestTwo as dw
from study_case.pytest_skip.debug.debug_test_3 import DebugTestThree as dt


class Test1:

    def explanation(self):
        """
        按照指定顺序执行测试用例
        """

    @pytest.mark.run(order=5)
    def test_1(self):
        self.one1 = do().debug_test_1()

    @pytest.mark.run(order=0)
    def test_2(self):
        self.one2 = do().debug_test_2()

    @pytest.mark.run(order=1)
    def test_3(self):
        self.two3 = dw().debug_test_3()

    @pytest.mark.run(order=-1)
    def test_4(self):
        self.two4 = dw().debug_test_4()

    @pytest.mark.run(order=-5)
    def test_5(self):
        self.three5 = dt().debug_test_5()

    def test_6(self):
        self.three6 = dt().debug_test_6()


if __name__ == '__main__':
    pytest.main(["-v", "-s", "pytest_test_1.py"])
