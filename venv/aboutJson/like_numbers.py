#!/usr/bin/env python 
# coding:utf-8
import json

def get_like_numbers():
    filename = "likenumber.json"
    try:
        with open(filename) as f_obj:
            likenumber = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return likenumber

def create_like_numbers():
    likenumber = input("what's your favorite number?")
    filename = "likenumber.json"
    with open(filename,"w") as f_obj:
        json.dump(likenumber,f_obj)
    return likenumber

def greet_like_number():
    """读取文件并问候"""
    likenumber = get_like_numbers()
    if likenumber:
        print("I know your favorite number! It's "+likenumber+"!")
    else:
        likenumber = create_like_numbers()
        print("I know your favorite number! It's " + likenumber + "!")

greet_like_number()