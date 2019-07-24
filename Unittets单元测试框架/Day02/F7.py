# -*- coding:utf-8 -*-
# Author:D.Gray
import unittest,time
from selenium import webdriver

class BaiDuLink(unittest.TestCase):
    '''百度首页链接测试类'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get("http://www.baidu.com")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_baidu_newa(self):
        self.driver.find_element_by_link_text("新闻").click()
        self.driver.back()

    def test_baidu_map(self):
        self.driver.find_element_by_link_text("地图").click()
        self.driver.back()


class BaiDuSearch(unittest.TestCase):
    '''百度首页搜索测试类'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get("http://www.baidu.com")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_baidu_search(self):
        self.driver.find_element_by_id("kw").send_keys("webdriver")
        time.sleep(15)
        self.driver.back()

if __name__ == '__main__':
    suitte = unittest.TestLoader().loadTestsFromModule("F7.py")
    # suitte = unittest.TestLoader().loadTestsFromTestCase(BaiDuSearch)
    unittest.TextTestRunner(verbosity=2).run(suitte)
