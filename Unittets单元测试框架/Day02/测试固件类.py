# -*- coding:utf-8 -*-
# Author:D.Gray
import unittest,time
from selenium import webdriver

class Init(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get("http://www.baidu.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()