# -*- coding:utf-8 -*-
# Author:D.Gray
import os
import unittest
from selenium import webdriver

class F2(unittest.TestCase):
    '''
    通过setUpClass方法可以只打开一次Chrome浏览器进行自动化测试
    '''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()   #窗口最大化
        cls.driver.implicitly_wait(60)  #等待30秒
        cls.driver.get("http://www.baidu.com")

    def tearDownClass(cls):
       cls.driver.quit()

    def test_baidu_news(self):
        self.driver.find_element_by_link_text("新闻").click()  #通过link来定位
        self.driver.back()

    def test_baidu_map(self):
        self.driver.find_element_by_link_text("地图").click()
        # self.driver.find_element_by_partial_link_text("地图")  关键字匹配
        self.driver.back()

if __name__ == '__main__':
    unittest.main(verbosity=2)
