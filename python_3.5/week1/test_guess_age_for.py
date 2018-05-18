#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tkk1234
# @Date:   2018-05-11 10:40:35
# @Last Modified by:   tkk1234
# @Last Modified time: 2018-05-11 11:11:44
age = 20
for x in range(3):
	#如果<3条件成立，即循环开始（有条件为真）。通俗点讲：循环执行下面的代码3次直到猜对才停止.
	guess_age = int(input("pls enter my age:"))  #input输入数字实际上是字符串，所以要加int转换类型。
# 是否是字符还是数字可以用print(type(guess_age))来检验
	if guess_age == age:  #20如果不加引号代表数字，如果加了表示字符串
		print("you got it!")
		break    #猜对了就断开
	elif guess_age > age:
		print("no")
	elif guess_age < age:
		print("no")

else: # 或if count == 3:
	print("You have tried too many times!")
