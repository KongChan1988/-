# -*- coding:utf-8 -*-
# Author:D.Gray
import requests
from requests.auth import HTTPBasicAuth
r = requests.get(url="https://ecapi.parkingwang.com/v5/login",auth = ("wuya","admin"))
d = requests.get(url="https://ecapi.parkingwang.com/v5/login",auth = HTTPBasicAuth("wuya","admin"))
print(r.text)