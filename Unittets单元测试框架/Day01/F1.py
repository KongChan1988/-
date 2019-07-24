# -*- coding:utf-8 -*-
# Author:D.Gray
import unittest
class F1(unittest.TestCase):
    '''
    执行过程：先执行setUp  在执行 test_001  在执行 tearDown
    本次案例中实际输出结果 setUp test_001 tearDown  setUP test_002 tearDown ...
    '''
    def setUp(self):
        print("我已经做好了准备工作")

    def tearDown(self):
        print("已处理")

    def test_001(self):
        admin
        print("test1")

    def test_002(self):
        print("test2")

    def test_003(self):
        self.assertEqual(1,"1")

if __name__ == '__main__':
    unittest.main(verbosity=2)