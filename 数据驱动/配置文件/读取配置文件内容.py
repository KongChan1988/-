# -*- coding:utf-8 -*-
# Author:D.Gray
import configparser
def getLinux():
    list = []
    config = configparser.ConfigParser()  #实例化configparser
    config.read("config.ini")           #读取配置文件
    ip = config.get("Linux","ip")       #获取配置文件中 Linux节点 下的IP字段
    port = config.get("Linux", "PORT")
    username = config.get("Linux", "USERNAME")
    password = config.get("Linux", "PASSWORD")
    list.append(ip)
    list.append(port)
    list.append(username)
    list.append(password)
    return list
print(getLinux())