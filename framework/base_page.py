#！/usr/bin/python3.6
# -*- coding: utf-8 -*-
#@Time   :2019/1/10 09:38
#@Author :zkf8381

import time,pymysql
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import os.path
from framework.logger import Logger

# 创建一个日志实例
logger = Logger(logger="BasePage").getlog()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法
    """

    def __init__(self, driver):
        self.driver = driver

        #get an url link
    def open(self,url):
        self.driver.get(url)

        #quit browser and end testing
    def quit_browser(self):
        self.driver.quit()

        # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

        # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

        # 显示等待
    def wait(self,loc,seconds):
        try:
            wait_=WebDriverWait(self.driver,seconds)
            wait_.until(lambda driver:driver.find_element(*loc))
            logger.info("wait for %d seconds." % seconds)
        except NameError as e:
            logger.error("Failed to load the element with %s" % e)

        # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)

        # 保存图片
    def get_windows_img(self):
        """
        把file_path保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + 'Selenium/screenshots/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

         # 定位元素方法
    def find_element(self,loc):
        """
        :return: element
        """
        return self.driver.find_element(*loc)

        # 输入
    def send_keys(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to select in input box with %s" % e)
            self.get_windows_img()

        # 清除文本框
    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

        # 点击元素
    def click(self, selector):

        el = self.find_element(selector)
        try:
            el.click()
            logger.info("The element \'%s\' was clicked." % el.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

        #选择方法（下拉框元素定位选择）
    def selecte(self,loc,sloc):
        self.click(loc)
        try:
            self.click(sloc)
            pass
        except Exception as e:
            logger.error("Failed to select box with %s" % e)
            self.get_windows_img()

    # 选择方法（下拉框选项固定选择）
    def selectf(self, loc, value):
        select = self.find_element(loc)
        sel_obj = Select(select)
        if isinstance(value, int):
            sel_obj.select_by_index(value)
        elif isinstance(value, int):
            sel_obj.select_by_visible_text(value)

        #鼠标事件（左键点击）
    def move_element(self,loc,sloc):
        mouse=self.find_element(loc)
        try:
            ActionChains(self.driver).move_to_element(mouse).perform()
            self.click(sloc)
            pass
        except Exception as e:
            logger.error("Failed to click move_element with %s" % e)
            self.get_windows_img()

    def db_connect(self,sql):
        """
        连接数据库
        :param sql:
        :return:
        """
        db = pymysql.connect("192.168.6.48","root","123456","test")
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
            data = cursor.fetchone()
        except:
            db.rollback()
        db.close()

        return data

        # 强制等待
    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)