#!/usr/bin/env python 
# coding:utf-8
import requests
import json
from requests.auth import HTTPBasicAuth
# r=requests.get('http://www.baidu.com/s',params={'wd':'hhu'})
# r=requests.get('http://www.baidu.com/s',headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'})
# print('status:%s' % r.status_code)
# print(r.text)

a=HTTPBasicAuth('8a8d8ad2-67b3-4e19-920d-d5b315841736','dIZCNFi6AjRyUbr0')

# headers={
#     "Authorization":"auth"
# }
data={
    "scope":"basic",
    "state":"test_client_token"
}
r=requests.post('https://https://apis-mix.test.maxhub.vip/passport/api/token?grant_type=client_credentials',auth=a,json=data)
print(r.text.json())

# url1 = "http://https://apis-mix.test.maxhub.vip/passport/api/token?grant_type=client_credentials&state=xyz"
# response1 = requests.post(url1, auth=HTTPBasicAuth('8a8d8ad2-67b3-4e19-920d-d5b315841736', 'dIZCNFi6AjRyUbr0'))
# client_token = json.loads(response1.text)['access_token']
# print(client_token)