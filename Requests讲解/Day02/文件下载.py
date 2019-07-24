# -*- coding:utf-8 -*-
# Author:D.Gray
import requests,os,time
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                        " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
           "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
r = requests.get(url="https://mmxzqxl1.com/common/all/201903/SEXJWSLC/SEXJWSLC.rmvb",headers=headers,stream=True,verify=False)
now = time.strftime("%Y-%m-%d %H_%M_%S")
file_path = os.path.join("files","%s.rmvb"%now)
if r.status_code == 200:
    with open(file_path,"wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)
print(r.content.decode("utf-8"))