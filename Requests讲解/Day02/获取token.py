# -*- coding:utf-8 -*-
# Author:D.Gray
import requests
headers = {
    "Parkingwang-Client-Source":"ParkingWangAPIClientWeb",
    "Content-Type":"application/json;charset=UTF-8"
}
data= {
	"source": "common",
	"password": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
}
def login():
    '''
    获取动态token值
    :return:
    '''
    r = requests.post(url="https://ecapi.parkingwang.com/v5/login",json=data,headers=headers)
    gettoken = r.json()["data"]["token"]
    print(gettoken)
    return gettoken
login()
def Info():
    '''带token值发起请求'''
    r = requests.post(url="https://ecapi.parkingwang.com/v5/InfoGet",json={"token":login()},headers=headers)
    print(r.text)
Info()

