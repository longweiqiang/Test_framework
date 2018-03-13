#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 11:35
# @Author  : Weiqiang.long
# @Site    : 
# @File    : baidu_result_page.py
# @Software: PyCharm

from selenium.webdriver.common.by import By
from test.page.baidu_main_page import BaiDuMainPage


class BaiDuResultPage(BaiDuMainPage):
    loc_result_links = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    @property
    def result_links(self):
        return self.find_elements(*self.loc_result_links)





