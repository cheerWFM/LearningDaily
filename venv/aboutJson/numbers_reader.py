#!/usr/bin/env python 
# coding:utf-8
import json

filename = "numbers.json"

with open(filename) as f_obj:
    # 将列表读进内存中并存储到变量numbers中
    numbers = json.load(f_obj)
print(numbers)