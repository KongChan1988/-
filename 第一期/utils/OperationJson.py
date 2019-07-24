# _*_ coding:utf-8 _*_
# Author:D.Gray
import json
from utils.OperationExcel import WorkExcel
from config.Setting import DB_PATH

class WorkJson(object):

    def __init__(self):
        self.Excel = WorkExcel()
        self.file = DB_PATH("data","data.json")

    def ReadJson(self,row,kd):
        '''读取Json文件'''
        with open(self.file,"r",encoding="utf-8") as f:
            data = json.load(f)
            dic = data[self.get_Data(row=row)]
            dic["kd"] = kd
        return json.dumps(dic)

    def get_Data(self,row):
        '''从Work_Excel类中获取测试参数'''
        self.data = self.Excel.get_TestData(row)
        return self.data

# work = WorkJson()
# print(work.ReadJson(row=1,kd="性能测试"),type(work.ReadJson(row=1,kd="性能测试")))
