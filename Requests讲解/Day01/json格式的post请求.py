# -*- coding:utf-8 -*-
# Author:D.Gray
import requests,json
postdata = {"username": "","password":""}
heads = {"Content-Type":"application/json;charset=UTF-8",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/74.0.3729.169 Safari/537.36",
         "Parkingwang-Client-Source":"ParkingWangAPIClientWeb"}
r = requests.post(url="https://ecapi.parkingwang.com/v5/login",data=json.dumps(postdata),headers=heads)
print(json.dumps(r.json(),indent=True,ensure_ascii=False))