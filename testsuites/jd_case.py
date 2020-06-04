#！/usr/bin/python3.6

# -*- coding: utf-8 -*-
#@Time   :2019/1/12 14:51
#@Author :zkf8381

import time
from testsuites.test_base import TestBase
from pageobjects.jd_page import NewsPage


class News(TestBase):

    def test_news(self):

        news = NewsPage(self.driver)
        news.open('https://www.jd.com/')
        news.click_new()
        self.driver.switch_to.window(self.driver.window_handles[1])
        news.get_windows_img()
        time.sleep(2)