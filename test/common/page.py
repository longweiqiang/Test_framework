#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 11:30
# @Author  : Weiqiang.long
# @Site    : 
# @File    : page.py
# @Software: PyCharm

import time
from selenium.webdriver.common.action_chains import ActionChains
from test.common.browser import Browser
from utils.log import logger


class Page(Browser):
    def __init__(self, page=None, browser_type='firefox'):
        if page:
            self.dr = page.dr
        else:
            super(Page, self).__init__(browser_type=browser_type)

    @property
    def current_window(self):
        return self.dr.current_window_handle

    @property
    def title(self):
        return self.dr.title

    @property
    def current_url(self):
        return self.dr.current_url

    def get_driver(self):
        return self.dr

    def wait(self, seconds=3):
        time.sleep(seconds)

    def execute(self, js, *args):
        self.dr.execute_script(js, *args)

    def move_to(self, element):
        ActionChains(self.dr).move_to_element(element).perform()

    def find_element(self, *args):
        return self.dr.find_element(*args)

    def find_elements(self, *args):
        return self.dr.find_elements(*args)

    def switch_to_window(self, partial_url='', partial_title=''):
        """切换窗口
            如果窗口数<3,不需要传入参数，切换到当前窗口外的窗口；
            如果窗口数>=3，则需要传入参数来确定要跳转到哪个窗口
        """
        all_windows = self.dr.window_handles
        if len(all_windows) == 1:
            logger.warning('只有1个window!')
        elif len(all_windows) == 2:
            other_window = all_windows[1 - all_windows.index(self.current_window)]
            self.dr.switch_to.window(other_window)
        else:
            for window in all_windows:
                self.dr.switch_to.window(window)
                if partial_url in self.dr.current_url or partial_title in self.dr.title:
                    break
        logger.debug(self.dr.current_url, self.dr.title)

    def switch_to_frame(self, param):
        self.dr.switch_to.frame(param)

    def switch_to_alert(self):
        return self.dr.switch_to.alert