# -*- coding:utf-8 -*-
# Author:D.Gray
import requests
def getHeards():
    heards = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
              "Content-Type":"application/x-www-form-urlencoded"}
    return heards

data = {
    "origURL":"http://www.renren.com/home",
    "domain":"renren.com",
    "email":"15618285621",
    "icode":"",
    "key_id":1,
    "captcha_type":"web_login",
    "password":"5bef1a5df91f38a831d54e803f5802715d45151238957d736ec5e623926f95e5",
    "rkey":"5e0b20645efb740942b773a52d118eb9",
    "f":"https%3A%2F%2Fwww.baidu.com%2Flink%3Furl"
        "%3DCPGUXSzmc9jI1MNlIYTQTnvV4H0BfttSNeQDZQs-2wC%26wd%3D%26eqid%3Dbcdd206a0000f13a000000045d0a4528"
}

def login():
    '''登录后获取cookies'''
    r = requests.post(url="http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019532222641"
                      ,data=data,headers = getHeards())
    print(r.cookies)
    return r.cookies
login()
def getInfo():
    '''带着获取的cookies对服务端“个人”发起请求'''
    r = requests.get(url="http://www.renren.com/812850923/profile",cookies=login())
    print(r.text)
getInfo()