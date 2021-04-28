#!/usr/bin/env python 
# coding:utf-8
import logging

def div():
    try:
        print('请输入a的值：')
        a=float(input())
        if isinstance(a,float):
            r=10/int(a)
            print("result:",r)
    except Exception as a:
        logging.exception(a)
    except Exception as e:
        logging.exception(e)
    finally:
        print('finally...')

if __name__=='__main__':
    div()
    print('执行结束。。。')


