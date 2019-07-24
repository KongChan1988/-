# -*- coding:utf-8 -*-
# Author:D.Gray
import ddt,unittest,requests
url = "https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false"

headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
          "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
          "Referer":"https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95?city=%E4%B8%8A%E6%B5%B7&cl=false&fromSearch=true&labelWords=&suginput=",
           "Cookie":"user_trace_token=20190607175851-de786141-c53c-4c75-ba8c-d9d9beb89458; _ga=GA1.2.529630118.1559901538; LGUID=20190607175852-da9b38a2-890a-11e9-aa82-525400f775ce; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216b3160ae50195-0707aac08ee122-e353165-1327104-16b3160ae51152%22%2C%22%24device_id%22%3A%2216b3160ae50195-0707aac08ee122-e353165-1327104-16b3160ae51152%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22m_cf_cpt_baidu_pcbt%22%7D%7D; index_location_city=%E4%B8%8A%E6%B5%B7; LG_HAS_LOGIN=1; _gid=GA1.2.831476806.1562075559; LGSID=20190702215239-a7eaf13d-9cd0-11e9-bc12-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595%3Fcity%3D%25E4%25B8%258A%25E6%25B5%25B7%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; _gat=1; JSESSIONID=ABAAABAAAFCAAEGB0420BF9477A8933FDE675A40B12AF97; SEARCH_ID=ddcffec9f827466d965f0c2bbd81250a; X_HTTP_TOKEN=153db84c65004abb9075702651cd2675cbea41fd5b; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1561900839,1561901727,1562075560,1562075710; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1562075710; LGRID=20190702215509-015ca62b-9cd1-11e9-a4d6-5254005c3644"
          }

@ddt.ddt
class laGou(unittest.TestCase):
    @ddt.data((1,),(2,),(3,),(4,),(5,))
    @ddt.unpack
    def test_laGuou(self,pange):
        r = requests.post(url=url,headers=headers,data={"first":False,"kd":"自动化测试","pn":pange})
        self.assertEqual(r.json()["success"],True)
        city = r.json()["content"]["positionResult"]["result"][0]["city"]
        print(city)
if __name__ == '__main__':
    unittest.main(verbosity=2)