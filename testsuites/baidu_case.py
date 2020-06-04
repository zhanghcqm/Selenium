#！/usr/bin/python3.6

# -*- coding: utf-8 -*-
#@Time   :2019/1/12 14:23
#@Author :zkf8381
import time
from testsuites.test_base import TestBase
from pageobjects.baidu_page import Cloud

class BaiduSearch(TestBase):

    def test_baidu_search(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        input = Cloud(self.driver)
        input.open('https://www.baidu.com/')
        input.value_input('selenium')  # 调用页面对象中的方法
        input.submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        input.get_windows_img()  # 调用基类截图方法
        try:
            assert 'selenium' in 'selenium'
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))


