#!/usr/bin/env python 
# coding:utf-8

import xlrd

def GetInfoFromXls(file):
    """打开excle表格"""
    workbook = xlrd.open_workbook(file)
    print(workbook)

    """获取sheet名称"""
    sheet_names = workbook.sheet_names()
    print(sheet_names)


    # 获得所有的sheet对象
    sheets_obj = workbook.sheets()
    print(sheets_obj)


    # 通过index获得第一个sheet对象
    sheet1_obj = workbook.sheet_by_index(0)

    # 通过sheet名获得sheet对象
    # sheet1_obj = workbook.sheet_by_name('')
    # print(sheet1_obj)

GetInfoFromXls('test.xls')





