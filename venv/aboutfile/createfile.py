#!/usr/bin/env python 
# coding:utf-8

with open('../../hello.txt', 'a+') as f:
    f.writelines('这是神iukjhik\n')
    seq={'h\n','shfuhf\n','nudsfh'}
    a=f.writelines(seq)
    print(a)
    print(type(a))


