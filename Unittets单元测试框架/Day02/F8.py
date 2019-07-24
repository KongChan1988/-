# -*- coding:utf-8 -*-
# Author:D.Gray
import unittest,time
from Unittets单元测试框架.Day02.测试固件类 import Init
class BaiDuLink(Init):
    @unittest.skip("暂不执行此用例")
    def test_news(self):
        self.driver.find_element_by_link_text("新闻").click()
        self.driver.back()
    def test_map(self):
        self.driver.find_element_by_link_text("地图").click()
        self.assertEqual(self.driver.title,"百度新闻——海量中文资讯平台")
        self.driver.back()
    @staticmethod
    def suitte():
        suitte = unittest.TestSuite(unittest.makeSuite(BaiDuLink))
        return suitte
class BaiDuSearch(Init):
    '''百度首页搜索测试类'''
    def test_baidu_search(self):
        self.driver.find_element_by_id("kw").send_keys("webdriver")
        time.sleep(15)
        self.driver.back()
    @staticmethod
    def suitte():
        suitte = unittest.TestSuite(unittest.makeSuite(BaiDuSearch))
        return suitte
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(BaiDuLink.suitte())