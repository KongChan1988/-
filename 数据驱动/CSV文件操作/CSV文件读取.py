# -*- coding:utf-8 -*-
# Author:D.Gray
import csv
def readList():
    '''列表形式读取csv文件内容'''
    with open("csv.csv","r") as f:
        reader = csv.reader(f)
        next(reader)            #忽略一行数据内容
        for item in reader:
            print(item)
readList()
def readDict():
    '''字典形式读取csv'''
    with open("csv.csv",'r') as fe:
        reader = csv.DictReader(fe)
        for item in reader:
            print(dict(item))
readDict()