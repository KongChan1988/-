# _*_ coding:utf-8 _*_
# Author:D.Gray
import requests,lxml,urllib3
from utils.OperationExcel import WorkExcel
from utils.OperationJson import WorkJson

class Methods(object):
    def __init__(self):
        self.Excel = WorkExcel()
        self.Json = WorkJson()
        self.session = requests.Session()

    def PostHead(self):
        head = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Content-Type":"application/x-www-form-urlencoded",
            "Referer":"https://www.lagou.com/jobs/list_%E8%85%BE%E8%AE%AF?city=%E4%B8%8A%E6%B5%B7&cl=false&fromSearch=true&labelWords=&suginput=",
            "Cookie":"user_trace_token=20190711093244-7662e644-c0e4-4937-87e9-d2cd2405e4bc; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1563856272,1563859845,1563873582,1563931253; _ga=GA1.2.1765988979.1562808765; LGUID=20190711093245-c8c700c9-a37b-11e9-a4de-5254005c3644; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216bdea9bb364ed-09c96e21c7c409-14397640-1440000-16bdea9bb3856a%22%2C%22%24device_id%22%3A%2216bdea9bb364ed-09c96e21c7c409-14397640-1440000-16bdea9bb3856a%22%7D; _gid=GA1.2.37672380.1563759357; LG_LOGIN_USER_ID=2ef9a4cd8d366c968896dca04cabcc4ecfcc0d06919038a3; LG_HAS_LOGIN=1; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=380; gate_login_token=ba4a89777ce7161a12754cf6d7830c66c5d3b3aef14bec89; privacyPolicyPopup=false; index_location_city=%E4%B8%8A%E6%B5%B7; SEARCH_ID=0668229b66c644d2953b94966a05a456; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1563932229; X_HTTP_TOKEN=5dc2edb33c3a2dc492223936514e1640ec09468157; LGSID=20190724092053-47ee5639-adb1-11e9-82ad-525400f775ce; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=bzclk.baidu.com; PRE_SITE=http%3A%2F%2Fbzclk.baidu.com%2Fadrc.php%3Ft%3D06KL00c00fZNKw_0QW9b0FNkUsK8_WII00000cTH27C00000uNUKKc.THL0oUhY1x60UWdVUv4_py4-g1PxuAT0T1dhP1--P1TzP10snHF-nHTk0ZRqPYn4nW6vrjRdrHIaPRcsf163fWT4fWIjwjb4rD7AfH60mHdL5iuVmv-b5HnzPjnknHfsrH6hTZFEuA-b5HDv0ARqpZwYTZnlQzqLILT8UA7MULR8mvqVQvk9UhwGUhTVTA7Muiqsmzq1uy7zmv68pZwVUjqdIAdxTvqdThP-5ydxmvuxmLKYgvF9pywdgLKWmMf0mLFW5HcdP1RY%26tpl%3Dtpl_11534_19968_16032%26l%3D1512575879; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm_source%3Dm_cf_cpt_baidu_pcbt; LGRID=20190724093709-8da7a0c8-adb3-11e9-a4ef-5254005c3644; _putrc=6947C93439D8DFE6; JSESSIONID=ABAAABAAAFCAAEGE806AC385B860E69F121508E89119BDD; login=true; unick=%E7%8E%8B%E4%BC%9F; WEBTJ-ID=20190724092100-16c2191373730-06e83d41adf4328-14367940-1440000-16c2191373842b; TG-TRACK-CODE=search_code; _gat=1",
            "Connection":"keep-alive"
        }
        return head

    def GetHead(self):
        head = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Referer":"https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95?city=%E4%B8%8A%E6%B5%B7&cl=false&fromSearch=true&labelWords=&suginput=",
            "Cookie":"user_trace_token=20190711093244-7662e644-c0e4-4937-87e9-d2cd2405e4bc; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1563856012,1563856272,1563859845,1563873582; _ga=GA1.2.1765988979.1562808765; LGUID=20190711093245-c8c700c9-a37b-11e9-a4de-5254005c3644; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216bdea9bb364ed-09c96e21c7c409-14397640-1440000-16bdea9bb3856a%22%2C%22%24device_id%22%3A%2216bdea9bb364ed-09c96e21c7c409-14397640-1440000-16bdea9bb3856a%22%7D; _gid=GA1.2.37672380.1563759357; LG_LOGIN_USER_ID=2ef9a4cd8d366c968896dca04cabcc4ecfcc0d06919038a3; LG_HAS_LOGIN=1; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=380; gate_login_token=ba4a89777ce7161a12754cf6d7830c66c5d3b3aef14bec89; privacyPolicyPopup=false; index_location_city=%E4%B8%8A%E6%B5%B7; SEARCH_ID=6a7646a5806c4618b6dd679e8616e282; X_HTTP_TOKEN=5dc2edb33c3a2dc472047836514e1640ec09468157; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1563874027; LGRID=20190723172707-0a5598e1-ad2c-11e9-8228-525400f775ce; _putrc=6947C93439D8DFE6; JSESSIONID=ABAAABAABEEAAJA4BDFC81305C9D705D343CCA0D8C9FC12; login=true; unick=%E7%8E%8B%E4%BC%9F; WEBTJ-ID=20190723133056-16c1d4fad3cdb-004599b16340c18-14367940-1440000-16c1d4fad3d3ff; TG-TRACK-CODE=index_recjob; X_MIDDLE_TOKEN=495c286f2a5d81d3af28d861db78415b; LGSID=20190723171942-010d6423-ad2b-11e9-a4ee-5254005c3644; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=bzclk.baidu.com; PRE_SITE=http%3A%2F%2Fbzclk.baidu.com%2Fadrc.php%3Ft%3D06KL00c00fZNKw_0QW9b0FNkUs0hYHuI00000cTH27C00000uNUKKc.THL0oUhY1x60UWdVUv4_py4-g1IxuAT0T1d-ujN9nHNBn10snjFWmycd0ZRqPYn4nW6vrjRdrHIaPRcsf163fWT4fWIjwjb4rD7AfH60mHdL5iuVmv-b5HnzPjnknHfsrH6hTZFEuA-b5HDv0ARqpZwYTZnlQzqLILT8UA7MULR8mvqVQvk9UhwGUhTVTA7Muiqsmzq1uy7zmv68pZwVUjqdIAdxTvqdThP-5ydxmvuxmLKYgvF9pywdgLKWmMf0mLFW5Hm1njbv%26tpl%3Dtpl_11534_19968_16032%26l%3D1512575879; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm_source%3Dm_cf_cpt_baidu_pcbt",
             "Connection":"keep-alive"
        }
        return head

    def POST(self,row,search):
        try:
            request = self.session.post(url=self.Excel.get_TestUrl(row=row),
                                        headers = self.PostHead(),
                                        data=self.Json.ReadJson(row=row,kd=search),
                                        timeout = 6
                                        )
            return request.json()
        except Exception as e:
            raise EnvironmentError("接口发生异常:",e)

    def GET(self,url):
        try:
            request = self.session.get(url=url,
                                       headers = self.GetHead(),
                                       timeout = 6
                                       )
            return request
        except Exception as e:
            raise EnvironmentError("接口发生异常:",e)

    def IsCount(self,row,str2):
        self.expet = self.Excel.get_TestExpet(row=row)
        print("expet:",self.expet)
        flag = None
        if self.expet in str2:
            flag = True
        else:
            flag = False
        return flag


# work = Methods()
# print(work.POST(row=1,search="自动化测试"))
# print(work.IsCount(row=1,str2="'pageSize': 15"))

# print(work.GET(row=4))
