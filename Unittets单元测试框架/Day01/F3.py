# -*- coding:utf-8 -*-
# Author:D.Gray

import unittest
from selenium import webdriver

class F3(unittest.TestCase):
    '''
    setUP 和 setUpClass的区别就是
    setUP：执行多少个用例浏览器就打开关闭多少次
    setUpClass：不管执行多少个用例 浏览器就打开一次
    '''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("http://www.baidu.com")

    def tearDown(self):
        self.driver.quit()

    def test_baidu_news(self):
        self.driver.find_element_by_link_text("新闻").click()

    def test_baidu_map(self):
        self.driver.find_element_by_link_text("地图").click()

if __name__ == '__main__':
    unittest.main(verbosity=2)