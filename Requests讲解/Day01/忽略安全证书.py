# -*- coding:utf-8 -*-
# Author:D.Gray
import requests
# r = requests.get("http://www.baidu.com",timeout = 6 )  #6秒内响应到了URL则不报错
r = requests.get(url="https://www.12306.cn",verify = False)  #忽略安全证书
print(r.content.decode("utf-8"))

