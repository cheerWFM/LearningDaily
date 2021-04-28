#!/usr/bin/env python 
# coding:utf-8
while True:
    f = input("please input two number" + "\n" + "(you can input 'T' to exit)"+"\n")
    # 输入T 退出程序，不区分大小写
    if f == "T" or f == "t":
        break
    try:
        # 将输入的str 分割成单词
        number_list  = f.split()
        # 将str 转换成 int
        number_int = [int(x) for x in number_list]
        print(type(number_int[0]))

    # 输入文本，捕获错误并提示
    except ValueError:
        msg = "please input two number, it can not accept other character"
        print(msg)

    # 如果满足条件则将输入的整数求和并输出
    else:
        total = 0
        for ele in range(0,len(number_int)):
            total = total + number_int[ele]
        print(total)
