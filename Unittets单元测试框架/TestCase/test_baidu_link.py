# -*- coding:utf-8 -*-
# Author:D.Gray
import unittest,time
from Unittets单元测试框架.Day02.测试固件类 import Init
from selenium.webdriver.common.action_chains import ActionChains

class BaiDuLink(Init):
    '''百度首页超链接测试类'''
    def test_baidu_news(self):
        '''验证百度新闻链接'''
        self.driver.find_element_by_link_text("新闻").click()
        self.assertEqual(self.driver.title,"百度新闻——海量中文资讯")
        self.driver.back()

    def test_baidu_map(self):
        '''验证百度地图链接'''
        self.driver.find_element_by_link_text("地图").click()
        self.assertEqual(self.driver.title,"百度地图")
        self.driver.back()

    def test_baidu_hao123(self):
        '''验证百度hao123链接'''
        self.driver.find_element_by_link_text("hao123").click()
        self.assertEqual(self.driver.current_url, "https://www.hao123.com/")
        self.driver.back()

    def test_baidu_video(self):
        '''验证百度视频连接'''
        self.driver.find_element_by_link_text("视频").click()
        self.assertEqual(self.driver.title,"百度视频搜索——业界领先的中文视频搜索引之一")
        self.assertEqual(self.driver.current_url, "http://v.baid.com/")
        self.driver.back()

    def test_baidu_tieba(self):
        '''验证百度贴吧连接'''
        self.driver.find_element_by_link_text("贴吧").click()
        self.assertEqual(self.driver.title,"百度贴吧——全球最大的中文社区")
        self.assertEqual(self.driver.current_url, "https://tieba.baidu.com/index.html")
        self.driver.back()

    def test_baidu_academic(self):
        '''验证百度学术连接'''
        self.driver.find_element_by_link_text("学术").click()
        self.assertEqual(self.driver.title,"百度学术 - 保持学习的态度")
        self.assertEqual(self.driver.current_url, "http://xueshu.baidu.com/")
        self.driver.back()

    def test_baidu_moreproduct(self):
        '''验证百度更多产品连接'''
        so = self.driver.find_element_by_link_text("更多产品")
        ActionChains(self.driver).move_to_element(so).perform()
        time.sleep(5)
        self.driver.find_element_by_link_text("风云榜").click()
        self.assertEqual(self.driver.title,"百度搜索风云榜")
        self.driver.back()

    # def test_baidu(self):
    #     '''验证百度新鲜事连接'''
    #     so = self.driver.find_element_by_partial_link_text("百度")
    #     ActionChains(self.driver).move_to_element(so).perform()
    #     time.sleep(5)
    #     self.assertEqual(so.get_attribute("value"), "点击一下，了解更多")
    #     so.click()
    #     # self.assertEqual(self.driver.title,"今日新鲜事_百度搜索")
    #     # self.assertEqual(so.get_attribute("value"),"今日新鲜事")
    #     self.driver.back()

if __name__ == '__main__':
    unittest.main(verbosity=2)