#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 18:17
# @Author  : Weiqiang.long
# @Site    : 
# @File    : test_report.py
# @Software: PyCharm

import unittest
from BeautifulReport import BeautifulReport


class UnittestCaseSecond(unittest.TestCase):
    """ 测试代码生成与loader 测试数据"""

    def test_equal(self):
        """
            test 1==1
        :return:
        """
        import time
        time.sleep(1)
        self.assertTrue(1 == 1)

    @BeautifulReport.add_test_img('测试报告.png')
    def test_is_none(self):
        """
            test None object
        :return:
        """
        save_some_img('测试报告.png')
        self.assertIsNone(None)