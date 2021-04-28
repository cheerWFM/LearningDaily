#!/usr/bin/env python 
# coding:utf-8
def foo(c):
    n=int(c)
    if n==0:
        raise ValueError('invaild value:%s' % c)
    return 10/n
def bar():
    try:
        foo(0)
    except ValueError as e:
        print('valueError')
        raise
bar()

