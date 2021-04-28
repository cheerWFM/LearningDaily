#!/usr/bin/env python 
# coding:utf-8

import json
def greet_user():
    """读取名字并问候"""
    username = get_stored_username()
    if username:
        check = input("your name is "+username+", Do this name is right? (y/n)")

        if check == "y":
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
    else:
        username = get_new_username()
        print("welcome back, "+username+"!")


def get_stored_username():
    """如果存储了用户名则获取用户名"""
    filename = "username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("What's your name?")
    filename = "username.json"
    with open(filename,"w") as f_obj:
        json.dump(username,f_obj)
    return username


greet_user()