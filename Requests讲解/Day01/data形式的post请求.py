# -*- coding:utf-8 -*-
# Author:D.Gray
import requests,json
postdata = {"first":"true","pn":2,"kd":"自动化测试工程师"}
headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
           "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                        " Chrome/74.0.3729.169 Safari/537.36",
           "Referer":"https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95?city=%E4%B8%8A%E6%B5%B7&cl=false&fromSearch=true&labelWords=&suginput="}
r = requests.post(url="https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false",
                  data=postdata,headers=headers)
print(r.status_code)
text = r.json()
print(json.dumps(text,indent=True,ensure_ascii=False))
