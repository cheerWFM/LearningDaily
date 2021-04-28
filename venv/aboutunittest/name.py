#!/usr/bin/env python 
# coding:utf-8

def get_formatted_name(first,last,middle = '' ):
    """Genarate a neatly formatted full name"""
    if middle :
        full_name = first + " " + middle + " " + last
    else:
        full_name = first +" "+ last
    return full_name.title()

def get_name():
    print("Enter 'q' at any time to quit.")
    while True:
        first = input("\nPlease give me a first name:")
        if first == "q" or first == "Q":
            break
        last = input("please give me a last name:")
        if last == "q" or last == "Q":
            break
        formatted_name = get_formatted_name(first,last)
        print("\tNeatly formatted name:"+formatted_name+".")
