# -*- coding:utf-8 -*-
# Author:D.Gray
import xml.dom.minidom

def getXML(value):
    '''获取单节点的数据内容'''
    file = xml.dom.minidom.parse("data.xml")        #读取xml文件
    db = file.documentElement
    itemList = db.getElementsByTagName(value)       #获取节点名称
    item = itemList[0]                              #取节点第一个元素
    return item.firstChild.data                     #返回元素内容
print(getXML("admin"))

def getUser(value="WuYa",child=None):
    '''获取多节点的数据内容'''
    file = xml.dom.minidom.parse("data.xml")
    db = file.documentElement
    itemList = db.getElementsByTagName(value)   #获取父节点
    item = itemList[0]
    return item.getAttribute(child)     #获取子节点内容
print(getUser(child="nick"))