#!/usr/bin/env python 
# coding:utf-8
import xlwt

def CreateXls():
    xls = xlwt.Workbook()
    sheet = xls.add_sheet('Test data')
    sheet.write(0,0,'name')
    sheet.write(0,1,'age')
    sheet.write(0,2,'grender')
    name = ['温芳梅','谭松韵','刘昊然','hahahah']
    age = [12,45,67,35]
    grender = [0,2,1,3]
    i = 0
    j = 0
    q = 0
    for names in name:
        sheet.write(1,i,names)
        i+=1
    for ages in age:
        sheet.write(2,j,ages)
        j+=1

    for grenders in grender:
        sheet.write(3,q,grenders)
        q+=1

    xls.save('test.xls')

CreateXls()

