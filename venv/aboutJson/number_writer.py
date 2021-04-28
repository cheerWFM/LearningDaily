#!/usr/bin/env python 
# coding:utf-8
import json

numbers = [2,5,7,11,13]
filename = "numbers.json"
with open(filename,"w") as f_obj:
    # 将数字列表存储都文件numbers.json中
    json.dump(numbers,f_obj)