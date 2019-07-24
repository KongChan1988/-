# -*- coding:utf-8 -*-
# Author:D.Gray
import requests

paydata = {"search_text":"乌鸦","cat":1002}
r = requests.get(url="https://movie.douban.com/subject_search",params=paydata)  #向URL发送请求
print(r.status_code)   #获取协议状态码
print(r.text)           #获取响应数据HTML或JSON
print(r.url)            #获取当前URL地址
print(r.content.decode("utf-8"))    #获取字节流数据 返回的是二进制