#！/usr/bin/python3.6

# -*- coding: utf-8 -*-
#@Time   :2019/1/11 10:57
#@Author :zkf8381

from framework.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.logger import Logger

logger = Logger(logger="cloud_page").getlog()

class Cloud(BasePage):
    #定位器

    input_box = (By.ID,'kw')
    search_submit = (By.XPATH,'//*[@id="su"]')

    def value_input(self, text):
        self.wait(self.input_box,5)
        self.send_keys(self.input_box, text)

    def submit_btn(self):
        self.click(self.search_submit)
        logger.info("show results!")
        self.sleep(2)

