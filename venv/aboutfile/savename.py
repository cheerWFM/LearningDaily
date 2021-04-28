#!/usr/bin/env python 
# coding:utf-8


def SavePassnerName():
    f = input("please input your name!"+'\n')
    anser=input("why are you like coding?"+'\n')
    filename = '/Users/fangmeiwen/name.txt'
    ansername = '/Users/fangmeiwen/anser.txt'
    with open(filename, 'a+') as file_object:
        file_object.write(f + '\n')
    with open(ansername,'a+') as ansername_object:
        ansername_object.write(anser+'\n')

    while f is not None:
        print('hello~ welcome here')
        f= None


    with open(filename,'r') as file_object_1:
        fi = file_object_1.readlines()
        for line in fi:
            print(line.strip())

if __name__=='__main__':
    SavePassnerName()


