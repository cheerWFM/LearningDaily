#!/usr/bin/env python 
# coding:utf-8

print("Give me two numbers,and i'll division them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("second number:")
    try:
        answer= int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("you can't division by 0")
    else:
        print(answer)