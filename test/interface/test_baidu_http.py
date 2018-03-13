#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 16:10
# @Author  : Weiqiang.long
# @Site    : 
# @File    : test_baidu_http.py
# @Software: PyCharm

import unittest
from utils.config import Config, REPORT_PATH
from utils.client import HTTPClient
from utils.log import logger
from utils.HTMLTestRunner import HTMLTestRunner
from utils.assertion import assertHTTPCode


class TestBaiDuHTTP(unittest.TestCase):
    URL = Config().get('URL')

    def setUp(self):
        self.client = HTTPClient(url=self.URL, method='GET')

    def test_baidu_http(self):
        res = self.client.send()
        logger.debug(res.text)
        assertHTTPCode(res,[400])
        self.assertIn('百度一下，你就知道', res.text)


if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        r = Config().get('report')
        runner = HTMLTestRunner(f, verbosity=r.get('verbosity'),
                                title=r.get('title'),
                                description=r.get('description'))
        runner.run(TestBaiDuHTTP('test_baidu_http'))