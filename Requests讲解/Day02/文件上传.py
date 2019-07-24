# -*- coding:utf-8 -*-
# Author:D.Gray
import requests,os
def headers():
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
              "Content-Type":"application/x-www-form-urlencoded"}
    return headers

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
    s = requests.Session()
    s.post(url="http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019532222641",
           data=data,headers=headers()
           )
    return s

f_data = {
"upload":"提交",
"__channel":"renren",
"privacyParams":{"sourceControl": 99},
"hostid":812850923,
"requestToken":220657126,
"_rtk":"d8e7f440"
}
file_path = os.path.join("files","171170.jpg")
print(file_path)
files = {"file":("171170.jpg",open(file_path,"rb"),"image/jpeg",{})}
file_headers = {"Content-Type":"multipart/form-data;",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
def fileUp():
    r = login().post(url="http://upload.renren.com/upload.fcgi?pagetype=addpublishersingle&hostid=812850923&callback=window.parent.handlePhotoData&uploadid=profile_publisher_photo_1560959356682",
                     headers = file_headers,files = files)
    print(r.text)
fileUp()

