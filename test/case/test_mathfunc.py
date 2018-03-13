#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 16:47
# @Author  : Weiqiang.long
# @Site    : 
# @File    : test_mathfunc.py
# @Software: PyCharm

import unittest
from test.case.mathfunc import *

class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    def setUp(self):
        print("准备测试环境")

    def tearDown(self):
        print("还原测试环境")

    def test_add(self):
        """Test method add(a, b)"""
        print("add")
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        """Test method minus(a, b)"""
        print("minus")
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        print("multi")
        self.assertEqual(6, multi(2, 3))

    """
    skip装饰器一共有三个 unittest.skip(reason)、unittest.skipIf(condition, reason)、
    unittest.skipUnless(condition, reason)，skip无条件跳过，skipIf当condition为True时跳过，
    skipUnless当condition为False时跳过
    """
    @unittest.skip("跳过此cese，不执行")
    def test_divide(self):
        """Test method divide(a, b)"""
        print("divide")
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 3))

# if __name__ == '__main__':
#     unittest.main(verbosity=2)








