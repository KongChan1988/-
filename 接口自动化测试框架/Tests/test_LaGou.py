# _*_ coding:utf-8 _*_
# Author:D.Gray

import unittest
from bs4 import BeautifulSoup
from utils.OperationExcel import WorkExcel
from utils.OperationJson import WorkJson
from base.Method import Methods
from utils.public import Public


class TestLaGou(unittest.TestCase):

    def setUp(self):
        self.Excel = WorkExcel()
        self.Json = WorkJson()
        self.Method = Methods()
        self.Url = Public().positionURL()

    def statusCode(self,count,row):
        self.assertEqual("code",0)
        self.assertTrue(self.Method.IsCount(row=row,str2=count.text))

    def test_LagGou_001(self):
        '''测试翻页'''
        r = self.Method.POST(row=1,search="自动化测试")
        self.statusCode(row=1,count=r)

    def test_LagGou_002(self):
        '''关键字搜索'''
        r = self.Method.POST(row=1,search="性能测试工程师")
        self.statusCode(row=1,count=r)

    def test_LagGou_003(self):
        '''公司详情用例'''
        list = []
        for item in self.Url:
            r = self.Method.GET(url=item)
            r.encoding = r.apparent_encoding
            soup = BeautifulSoup(r.text,features="html.parser")
            target = soup.find("h2",class_="name").text     #定位某标签元素
            # list.append(target)
            # print("target:",target)
            # print("list:",list[0])
            self.assertTrue(self.Method.IsCount(row=4,str2=target))     #断言Excel文件中预期结果与实际结果是否为True
        self.Excel.WriteExcel(row=4,content="pass")

# t = TestLaGou()
# t.test_LagGou_003()