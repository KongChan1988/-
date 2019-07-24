# -*- coding:utf-8 -*-
# Author:D.Gray
import unittest,time
from Unittets单元测试框架.Day02.测试固件类 import Init

class BaiDuSearch(Init):
    '''百度首页搜索测试类'''
    def test_baidu_search(self):
        '''验证百度搜索框是否能赋值'''
        so = self.driver.find_element_by_id("kw")
        self.assertTrue(so.is_enabled())   #断言搜索框是否能赋值

    def test_baidu_so(self):
        '''验证在搜索框中输入测试参数'''
        so = self.driver.find_element_by_id("kw")
        so.send_keys("空蝉")
        time.sleep(5)
        # print(so.get_attribute("value"))
        self.assertEqual(so.get_attribute("value"),"空蝉")  #获取搜索框中的Value值并做断言

    @staticmethod
    def suitte():
        suitte = unittest.TestSuite(unittest.makeSuite(BaiDuSearch))
        return suitte
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(BaiDuSearch.suitte())