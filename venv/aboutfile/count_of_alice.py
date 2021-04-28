#!/usr/bin/env python 
# coding:utf-8

def CountWords(filename):
    '''计算一个文件中大致包含多少单词'''
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()

    # 捕获文件不存在的异常

    except FileNotFoundError:
        # msg = "Sorry,the file"+filename+"does not exist in current directory"
        # print(msg)
        # 将不存在的文件名写入一个文件
        with open("missing_files.txt","a+") as mf_obj:
            mf_obj.write(filename)
    else:
        # 计算文件中大致包含多少单词

        words = contents.split() # 以空格分割单词
        num_words = len(words)
        print("The file "+filename+"has about "+str(num_words)+ " words.")


filenames = ["alice.txt","moby_dick.txt","little_women.txt","siddhartha.txt"]
for filename in filenames:
    CountWords(filename)
