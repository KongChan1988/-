# -*- coding:utf-8 -*-
# Author:D.Gray
import requests,json,csv
url = "https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false"

headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
          "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
          "Referer":"https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95?city=%E4%B8%8A%E6%B5%B7&cl=false&fromSearch=true&labelWords=&suginput=",
            "Cookie":"JSESSIONID=ABAAABAAAGGABCB62912A62B9C7FA70833C09F719173B5B; user_trace_token=20190711213349-b3f5825a-2c8f-42e6-950a-f997eb52fac1; LGUID=20190711213352-85e4e457-a3e0-11e9-be7d-525400f775ce; X_MIDDLE_TOKEN=37b19a58f61d44d37b35960575ee77d9; LG_LOGIN_USER_ID=9973e2cf46582a6392b1dd3a0cd9e3b488ec97a69595c65e; LG_HAS_LOGIN=1; _putrc=6947C93439D8DFE6; login=true; unick=%E7%8E%8B%E4%BC%9F; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=380; gate_login_token=1c22d4facb9dcd8d4219c992141b239defa1709d130832be; privacyPolicyPopup=false; _gat=1; X_HTTP_TOKEN=75d178a103393afa55455826515ae53070130a6c4b; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1562852035; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1562855458; LGSID=20190711213352-85e4e255-a3e0-11e9-be7d-525400f775ce; LGRID=20190711223055-7e4b1721-a3e8-11e9-be7f-525400f775ce; _ga=GA1.2.1547766836.1562852035; _gid=GA1.2.108356903.1562852035; SEARCH_ID=81bb8599c8324f31aaafd28dea293504; index_location_city=%E4%B8%8A%E6%B5%B7"
          }

def laGou(page):
    r = requests.post(url=url,headers=headers,data={"first":False,"kd":"自动化测试","pn":page})
    list = []
    # print(r.text)
    print(json.dumps(r.json(),indent=True,ensure_ascii=False))
    for i in range(15):
        companyFullName = r.json()["content"]["positionResult"]["result"][i]["companyFullName"]
        city = r.json()["content"]["positionResult"]["result"][i]["city"]
        salary = r.json()["content"]["positionResult"]["result"][i]["salary"]
        companySize = r.json()["content"]["positionResult"]["result"][i]["companySize"]
        linestaion = r.json()["content"]["positionResult"]["result"][i]["linestaion"]
        # print("公司名称：%s  城市：%s  薪资：%s  公司规模:%s  公司地址：%s"%(companyFullName,city,salary,companySize,linestaion))
        dicts = {"公司名称":companyFullName,"城市":city,"薪资":salary,"公司规模":companySize,"地址":linestaion}
        list.append(dicts)
    return list
laGou(1)
# def writeCSV():
#     title = ["公司名称","城市","薪资","公司规模","地址"]
#     for item in range(1,31):
#         postion = laGou(item)
#         with open("laGou.csv","a",newline="",encoding="gbk") as f:
#             writer = csv.DictWriter(f,title)
#             writer.writeheader()
#             writer.writerows(postion)
# writeCSV()