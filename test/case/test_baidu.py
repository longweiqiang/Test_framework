#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 11:38
# @Author  : Weiqiang.long
# @Site    : 
# @File    : baidu_test.py
# @Software: PyCharm

import time
import unittest
from utils.config import Config, REPORT_PATH, DATA_PATH
from utils.log import logger
from utils.file_reader import ExcelReader
from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Email
from test.page.baidu_result_page import BaiDuMainPage, BaiDuResultPage


class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu.xlsx'

    def sub_setUp(self):
        # 初始页面是main page，传入浏览器类型打开浏览器
        self.page = BaiDuMainPage(browser_type='chrome').get(self.URL, maximize_window=False)

    def sub_tearDown(self):
        self.page.quit()

    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.search(d['search'])
                time.sleep(2)
                self.page = BaiDuResultPage(self.page)  # 页面跳转到result page
                links = self.page.result_links
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()


if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        r = Config().get('report')
        runner = HTMLTestRunner(f, verbosity=r.get('verbosity'),
                                title=r.get('title'),
                                description=r.get('description'))
        runner.run(TestBaiDu('test_search'))

        runner = HTMLTestRunner(f, verbosity=2, title='测试报告', description='testreport')
        runner.run(TestBaiDu('test_search'))

    c = Config().get('mail')
    e = Email(title=c.get('title'),
              message=c.get('message'),
              receiver=c.get('receiver'),
              server=c.get('server'),
              sender=c.get('sender'),
              password=c.get('password'),
              path=report)
    e.send()





# if __name__ == '__main__':
#     report = REPORT_PATH + '\\report.html'
#     with open(report, 'wb') as f:
#         runner = HTMLTestRunner(f, verbosity=2, title='测试报告', description='testreport')
#         runner.run(TestBaiDu('test_search'))
#
#     c = Config().get('mail')
#     e = Email(title=c.get('title'),
#               message=c.get('message'),
#               receiver=c.get('receiver'),
#               server=c.get('server'),
#               sender=c.get('sender'),
#               password=c.get('password'),
#               path=report)
#     e.send()












