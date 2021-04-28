#!/usr/bin/env python 
# coding:utf-8
import requests
r=requests.get('http://www.baidu.com/')
print(r.status_code)
print(r.text)
print(r.encoding)
print(r.json())



