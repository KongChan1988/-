# _*_ coding:utf-8 _*_
# Author:D.Gray
import os,json
from config.Setting import DB_PATH
from utils.OperationExcel import WorkExcel
from utils.OperationJson import WorkJson

class Public(object):

    def __init__(self):
        self.Excel = WorkExcel()
        self.Json = WorkJson()

    def positionURL(self):
        '''读取positionID文件，并拼接URL地址'''
        list = []
        with open(DB_PATH("data","positionID")) as f:
            data = json.loads(f.read())
            for item in data:
                url ="https://www.lagou.com/jobs/%s.html"%item
                list.append(url)
        return list

# p = Public()
# print(p.positionURL(),type(p.positionURL()))

