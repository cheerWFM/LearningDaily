#!/usr/bin/env python 
# coding:utf-8
import json

filename = "username.json"
with open(filename) as f_obj:
    # json.load()将存储在username.json中到信息读取到变量username 中
    username = json.load(f_obj)
    print("welcome back, "+username+"!")