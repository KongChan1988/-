# -*- coding:utf-8 -*-
# Author:D.Gray
import unittest,time
from Unittets单元测试框架.Day02.测试固件类 import Init
class BaiDuLink(Init):
    def test_news(self):
        self.driver.find_element_by_link_text("新闻").click()
        self.assertEqual(self.driver.title,"百度新闻——海量中文资讯平台")
    def test_baidu_search(self):
        so = self.driver.find_element_by_id("kw")
        self.assertTrue(so.is_enabled())
    def test_baidu_title(self):
        self.assertIn("百度",self.driver.title)
if __name__ == '__main__':
    unittest.main(verbosity=2)