#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tkk1234
# @Date:   2018-05-09 16:52:58
# @Last Modified by:   tkk1234
# @Last Modified time: 2018-05-10 11:42:58
traffic_cost = 5 + 5 + 5
food_cost = 1 + 1 + 1
health_cost = 1 + 2 + 3 + 4

total = traffic_cost + food_cost + health_cost
print(total)

# 用户输入
name = input("What is your name?")
print(name)

#导入getpass库，不显示输入的密码
import getpass
username = input("username:")
password = getpass.getpass("password:")
#第一个getpass后面的点“.” 表示调用getpass的“getpass”的功能，言下之意就是getpass还可以调用很多其他功能。

#检验用户名密码是否正确
if username == "tkk1234" and password == "111111":
	print("yes you may in!")
else:
	print("all worng!please retry!")
