#！/usr/bin/python3.6

# -*- coding: utf-8 -*-
#@Time   :2019/1/11 16:24
#@Author :zkf8381

import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import os

# 定义输出的文件位置和名字
DIR = os.path.dirname(os.path.abspath(__file__))
now = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))

filename =now+"report.html"

testsuite = unittest.defaultTestLoader.discover(
	start_dir='./testsuites',
	pattern='*case.py',
	top_level_dir=None
	)

with open(DIR+'/test_report/'+filename,'wb') as f:
    runner = HTMLTestRunner(
    	stream=f,
    	verbosity=2, 
    	title='gateway UI report',
    	description='执行情况',
    	tester='zkf 8381'
	)
    runner.run(testsuite)

