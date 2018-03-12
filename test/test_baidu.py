#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 15:58
# @Author  : Weiqiang.long
# @Site    : 
# @File    : test_baidu.py
# @Software: PyCharm

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH, TEST_PATH, IMG_PATH
from utils.log import logger
from utils.file_reader import ExcelReader
from BeautifulReport import BeautifulReport
from lxml import etree

# URL = 'https://www.baidu.com'
# base_path = os.path.dirname(os.path.abspath(__file__)) + '\..'
# driver_path = os.path.abspath(base_path+'\drivers\chromedriver.exe')
#
# locator_kw = (By.ID, 'kw')
# locator_su = (By.ID, 'su')
# locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')
#
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get(URL)
# driver.find_element(*locator_kw).send_keys('selenium 灰蓝')
# driver.find_element(*locator_su).click()
# time.sleep(2)
# links = driver.find_elements(*locator_result)
# for link in links:
#     print(link.text)
# driver.quit()


'''
如果想要搜索“Python selenium”，是不是要再创建一个脚本？还是把原来的脚本修改一下？
或者我们可以用unittest来改一下，把两次搜索分别写一个测试方法
'''
class TestBaiDu(unittest.TestCase):
    # URL = 'https://www.baidu.com'
    URL = Config().get('URL')
    excel =DATA_PATH + '/baidu.xlsx'
    datas = ExcelReader(excel).data


    base_path = os.path.dirname(os.path.abspath(__file__)) + '\..'
    driver_path = os.path.abspath(base_path+'\drivers\chromedriver.exe')

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    @staticmethod
    def parse(html, xpath):
        """
            解析页面中的元素并返回一个对象
        :param xpath: 需要获取页面中的元素对应的xpath
        :param html: 页面的html元素
        :return:
        """
        return etree.HTML(html).xpath(xpath)

    def save_img(self, img_name):
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(IMG_PATH), img_name))

    def sub_setUp(self):
        self.dr = webdriver.Chrome(executable_path=self.driver_path)
        self.dr.get(self.URL)

    def sub_tearDown(self):
        self.dr.quit()

    @BeautifulReport.add_test_img('测试报告.png')
    def test_search_0(self):
        # datas = ExcelReader(self.excel).data
        for d in self.datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.dr.find_element(*self.locator_kw).send_keys(d['search'])
                self.dr.find_element(*self.locator_su).click()
                time.sleep(2)
                links = self.dr.find_elements(*self.locator_result)
                for link in links:
                    logger.info(link.text)
                    self.save_img('测试报告.png')
                self.sub_tearDown()

        # self.dr.find_element(*self.locator_kw).send_keys('selenium 灰蓝')
        # self.dr.find_element(*self.locator_su).click()
        # time.sleep(2)
        # links = self.dr.find_elements(*self.locator_result)
        # for link in links:
        #     # print(link.text)
        #     logger.info(link.text)

    # def test_search_1(self):
    #     self.dr.find_element(*self.locator_kw).send_keys('Python selenium')
    #     self.dr.find_element(*self.locator_su).click()
    #     time.sleep(2)
    #     links = self.dr.find_elements(*self.locator_result)
    #     for link in links:
    #         # print(link.text)
    #         logger.info(link.text)


if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover(TEST_PATH, pattern='test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告', description='测试deafult报告', log_path=REPORT_PATH)

















