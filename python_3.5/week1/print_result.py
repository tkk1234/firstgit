#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tkk1234
# @Date:   2018-05-10 11:42:53
# @Last Modified by:   tkk1234
# @Last Modified time: 2018-05-10 14:43:00
results = int(input("pls enter your digi number:"))
#必须顶行
#同一级代码缩进必须一致
#官方建议缩进4个

if results >= 1 and results <= 60:
	print("C")
elif results >= 60 and results <= 80:
	print("B")
elif results >= 90 and results <= 100:
	print("A")
	choice = input("pls choose a gift:cholocate,candy,cake： ")
	if choice == "cake":
		print("Here you go!")
else:
	print("you are out!")
