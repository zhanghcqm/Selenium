#！/usr/bin/python3.6

# -*- coding: utf-8 -*-
#@Time   :2019/1/13 14:54
#@Author :zkf8381

from selenium import webdriver
import unittest

class TestBase(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()   #驱动浏览器
        self.driver.implicitly_wait(10)  #设置隐式等待
        self.driver.maximize_window()    #最大化浏览器

    # def test(self):
    #     print('这是一个测试用例')

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()