# -*- coding:utf-8 -*-
# Author:D.Gray
import unittest,time
from selenium import webdriver

class F4(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get("http://www.baidu.com")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    '''百度首页链接测试'''
    def test_001(self):
        '''百度首页链接测试：验证新闻的链接'''
        self.driver.find_element_by_link_text("新闻").click()
        self.driver.back()

    def test_002(self):
        '''百度首页链接测试：验证地图的链接'''
        self.driver.find_element_by_link_text("sadwwe").click()
        self.driver.back()

    '''百度首页搜索测试'''
    def test_003(self):
        '''百度首页搜索测试：验证搜索功能'''
        self.driver.find_element_by_id("kw").send_keys("webdriver")
        time.sleep(30)
        self.driver.back()

if __name__ == '__main__':
    unittest.main(verbosity=2)