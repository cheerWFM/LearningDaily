#!/usr/bin/env python 
# coding:utf-8
import os.path
import time
from datetime import datetime


def create_file():
    now = datetime.now()
    time_str=now.strftime("%Y-%m-%d %H:%M:%S")
    filepath='/Users/fangmeiwen/Documents/'
    filename=time_str
    file_name=filepath+filename
    f=open(file_name,'w')
    f.write('现在的时间是：%s\n' % time_str)
    seq=['广州\n','上海\n','南京']
    f.writelines(seq)
    f.close()

if __name__=='__main__':
    create_file()

