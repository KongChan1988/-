# -*- coding:utf-8 -*-
# Author:D.Gray
import xlrd,os
'''xlrd，xlwt,xlutils适用xls后缀的Excel
    xlrd会把原文件内容先清空 类似(w)操作
'''

work = xlrd.open_workbook("data1.xls")   #打开excel文件
sheet = work.sheet_by_index(0)          #根据索引选择sheet
#查看文件中有内容的行数
print(sheet.nrows)
#查看文件中单元格内容
print(sheet.cell_value(5,1))    #获取第6行第2列单元格数据内容
