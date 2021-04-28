#!/usr/bin/env python
# coding:utf-8
from pip._vendor.distlib.compat import raw_input

count=0
filename='/Users/fangmeiwen/learning_python.txt'
with open(filename,'r+') as file_object:
    for line in file_object:
        s= file_object.readlines()
        print(s.strip())
        if 'love' in s:
            print("the string has the target")
            count+=0
        print("文件中一共存在%s 个 \"love\"" % count)
        print(type(s))



#
#     f= file_object.readlines()
#
# for line in f:
#     print(line.rstrip())
# print(type(f))


    # name=raw_input("please input your name" )
    # file_object.write("l love you \n")
    # file_object.write("I am lie")





