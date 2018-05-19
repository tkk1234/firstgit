#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tkk1234
# @Date:   2018-05-19 10:17:21
# @Last Modified by:   tkk1234
# @Last Modified time: 2018-05-19 19:45:19

data = open("C:/Users/iphone5s/Desktop/中文.txt",encoding="utf-8").read()
print(data)

f = open("C:/Users/iphone5s/Desktop/中文.txt",encoding="utf-8")  #打开的文件内存
# 对象赋值一个变量，通常变量名为f。这个方法叫做文件句柄
