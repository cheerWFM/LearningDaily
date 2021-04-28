#!/usr/bin/env python 
# coding:utf-8
import  socket
#创建一个socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(("baidu.com",80))

s.close()