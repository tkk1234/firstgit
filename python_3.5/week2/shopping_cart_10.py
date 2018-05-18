#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tkk1234
# @Date:   2018-05-15 16:09:17
# @Last Modified by:   tkk1234
# @Last Modified time: 2018-05-16 10:25:11
product_list = [
("Iphone",5800),
("Mac pro",9800),
("Bike",800),
("Watch",10600),
("Coffee",31),
("tkk1234 python",120),
]

shopping_list = []

salary = input("input your salary:")
if salary.isdigit():   #判断输入是否为数字，返回true或false。
	salary = int(salary)  #如果是，则转为int类型
	while True:
		for index,item in enumerate(product_list):  #打印产品下标，用来显示每个产品的序列号。
			print(index,item)
		user_choice = input("选择要买什么>>>:")
		if user_choice.isdigit():
			user_choice = int(user_choice)
			if user_choice < len(product_list) and user_choice >= 0: #判断列表的长度
				product_item = product_list[user_choice]
			if product_item[1] <= salary: #买的起
				shopping_list.append(product_item)
				salary -= product_item[1]
				print("product code [%s] is not exist!"% user_choice)
		elif user_choice == 'q':
			print("------shopping list------")
			for p in shopping_list:
				print(p)
			print("Your current balance:",salary)
			exit() #退出
		else:
			print("invalid option")
