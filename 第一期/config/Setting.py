# _*_ coding:utf-8 _*_
# Author:D.Gray
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.join(BASE_DIR,"data","demo.xls"))

Report_Path = os.path.join(BASE_DIR,"Report")
Tests_Path = os.path.join(BASE_DIR,"Tests")

def DB_PATH(pwd,filename):
    file_path = os.path.join(BASE_DIR,pwd,filename)
    return file_path


# print(DB_PATH(pwd="data",filename="demo.xls"))

