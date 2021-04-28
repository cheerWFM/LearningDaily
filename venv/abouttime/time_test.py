#!/usr/bin/env python 
# coding:utf-8

from datetime import datetime

#time=datetime.now()
# print(time)
# print(type(time))
#将时间转换成datetime格式
# create_time=datetime(2020,4,10,11,34,50)
# print(create_time)
#datetime转换成timestamp
# change=time.timestamp()l
#
# print(change)
# print(datetime.fromtimestamp(change))
# print(datetime.utcfromtimestamp(change))
def to_timestamp():
    print('请输入需要转换的日期：')
    text=input()
    #str转换成datetime
    cday=datetime.strptime(text,'%Y-%m-%d %H:%M:%S')
if isinstance(cday,datetime):
    print('类型正确')
    print(cday)
else:
    print('转换失败')




