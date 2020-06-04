#！/usr/bin/python3.6

# -*- coding: utf-8 -*-
#@Time   :2019/1/12 13:57
#@Author :zkf8381

from framework.base_page import BasePage
from selenium.webdriver.common.by import By


class NewsPage(BasePage):
    # 定位器
    moble_loc= (By.LINK_TEXT,'手机')
    moble_link = (By.LINK_TEXT,'对讲机')

    def click_new(self):
        self.wait(self.moble_loc,10)
        self.move_element(self.moble_loc,self.moble_link)


