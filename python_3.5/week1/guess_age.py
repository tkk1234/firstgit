#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tkk1234
# @Date:   2018-05-10 10:49:04
# @Last Modified by:   tkk1234
# @Last Modified time: 2018-05-10 17:35:30
age = 20
guess_age = int(input("pls enter my age:")) #input输入数字实际上是字符串，所以要加int转换类型。
# 是否是字符还是数字可以用print(type(guess_age))来检验
#
if guess_age == age:  #20如果不加引号代表数字，如果加了表示字符串
	print("you got it!")
elif guess_age > age:
	print("no")
elif guess_age < age:
	print("no")



