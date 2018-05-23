#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tkk1234
# @Date:   2018-05-23 17:33:08
# @Last Modified by:   tkk1234
# @Last Modified time: 2018-05-23 17:42:45
f = open("C:/Users/Administrator.USER-20170731GE/Desktop/云舞2.txt",'r',encoding="utf-8")

#读取前2行
# for x in range(2):
# 	print(f.readline())

#打印所有行
for line in f.readlines():
	print(line.strip()) #strip是去除左右空格

