#!/usr/bin/env python 
# coding:utf-8

filename = "alice.txt"
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "sorry,the file "+filename+"does not exist in current directory"
    print(msg)