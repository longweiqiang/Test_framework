#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 11:28
# @Author  : Weiqiang.long
# @Site    : 
# @File    : baidu_main_page.py
# @Software: PyCharm

from selenium.webdriver.common.by import By
from test.common.page import Page

class BaiDuMainPage(Page):
    loc_search_input = (By.ID, 'kw')
    loc_search_butthon = (By.ID, 'su')


    def search(self, kw):
        """搜索功能"""
        self.find_element(*self.loc_search_input).send_keys(kw)
        self.find_element(*self.loc_search_butthon).click()

