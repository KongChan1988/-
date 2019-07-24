# -*- coding:utf-8 -*-
# Author:D.Gray

import unittest,time
from selenium import webdriver

class BaiDuTest6(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(60)
        cls.driver.get("http://www.baidu.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    '''百度首页链接测试'''
    def test_baidu_news(self):
        '''百度首页链接测试：验证新闻链接'''
        self.driver.find_element_by_link_text("新闻").click()
        self.driver.back()

    def test_baidu_map(self):
        '''百度首页链接测试：验证地图链接'''
        self.driver.find_element_by_link_text("地图").click()
        self.driver.back()

    '''百度首页搜索'''
    def test_search(self):
        '''百度首页搜索：验证搜索功能'''
        self.driver.find_element_by_id("kw").send_keys("webdriver")
        time.sleep(30)
        self.driver.back()

if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(BaiDuTest6))  #实例化TestSuite()方法
    unittest.TextTestRunner(verbosity=2).run(suite)  #执行测试用例