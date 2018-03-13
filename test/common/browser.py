#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 10:41
# @Author  : Weiqiang.long
# @Site    : 
# @File    : browser.py
# @Software: PyCharm

"""
封装的选择浏览器、打开网址的类
"""

import time
import os
from selenium import webdriver
from utils.config import DRIVER_PATH, REPORT_PATH

CHROMEDRIVER_PATH = DRIVER_PATH + '\chromedriver.exe'
IEDRIVER_PATH = DRIVER_PATH + '\IEDriverServer.exe'
PHANTOMJSDRIVER_PATH = DRIVER_PATH + '\phantomjs.exe'

TYPES = {'firefox':webdriver.Firefox,
         'chrome':webdriver.Chrome,
         'ie':webdriver.Ie,
         'phantomjs':webdriver.PhantomJS}

EXECUTABLE_PATH = {'firefox':'wires',
                   'chrome':CHROMEDRIVER_PATH,
                   'ie':IEDRIVER_PATH,
                   'phantomjs':PHANTOMJSDRIVER_PATH}


class UnSupportBrowserTypeError(Exception):
    pass

class Browser(object):
    def __init__(self, browser_type='chrome'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise  UnSupportBrowserTypeError('仅支持%s!' % ','.join(TYPES.keys()))
        self.dr = None

    def get(self, url, maximize_window=True, implicitly_wait=30):
        self.dr = self.browser(executable_path=EXECUTABLE_PATH[self._type])
        self.dr.get(url)
        if maximize_window:
            self.dr.maximize_window()
        self.dr.implicitly_wait(implicitly_wait)
        return self

    def save_screen_shot(self, name='screen_shot'):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = REPORT_PATH + '\screenshot_%s' % day
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        screenshot = self.dr.save_screenshot(screenshot_path + '\\%s_%s.png' % (name,tm))
        return screenshot

    def close(self):
        self.dr.close()

    def quit(self):
        self.dr.quit()










