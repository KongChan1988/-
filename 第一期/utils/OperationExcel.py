# _*_ coding:utf-8 _*_
# Author:D.Gray
import xlrd
from xlutils.copy import copy
from config.Setting import DB_PATH

class WorkExcel(object):

    def __init__(self):
        self.work = xlrd.open_workbook(DB_PATH("data","demo.xls"))
        self.sheet = self.work.sheet_by_index(0)
        self.testID = 0
        self.testName = 1
        self.testURL = 2
        self.testData = 3
        self.testExpet = 4
        self.testResult = 5

    def get_AllRow(self):
        '''获取总行数'''
        return self.sheet.nrows

    def get_TestID(self,row):
        '''获取用例ID'''
        return self.sheet.cell_value(row,self.testID)

    def get_TestName(self,row):
        '''获取测试名'''
        return self.sheet.cell_value(row,self.testName)

    def get_TestUrl(self,row):
        '''获取请求地址'''
        return self.sheet.cell_value(row,self.testURL)

    def get_TestData(self,row):
        '''获取测试数据'''
        return self.sheet.cell_value(row,self.testData)

    def get_TestExpet(self,row):
        '''获取预期结果'''
        return self.sheet.cell_value(row,self.testExpet)

    def get_TestResult(self,row):
        '''获取实际结果'''
        return self.sheet.cell_value(row,self.testResult)

    def WriteExcel(self,row,content):
        '''写入实际结果'''
        self.old_work = copy(self.work)
        self.sheet = self.old_work.get_sheet(0)
        self.sheet.write(row,self.testResult,content)
        self.old_work.save(DB_PATH("data","demo.xls"))

# excel = WorkExcel()
# print(excel.get_TestUrl(2))
# excel.WriteExcel(1,"pass")