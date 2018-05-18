#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tkk1234
# @Date:   2018-05-17 11:31:40
# @Last Modified by:   tkk1234
# @Last Modified time: 2018-05-18 14:26:24
menu = {
	"北京":{
		"昌平":{
			"沙河":["oldboy","test"],
			"天通苑":["链家地产","我爱我家"],
		},
		"朝阳":{
			"望京":["奔驰","陌陌"],
			"国贸":["CICC","HP"],
			"东直门":["advent","飞信"],
		},
		"海淀":{},
},

	"山东":{
		"德州":{},
		"青岛":{},
		"济南":{},
	},
}

while  True:
	for x in menu:
		print(x)

	choice = input("选择进入>>:")
	if choice in menu:
		while True:
			for x in menu[choice]:
				print("\t",x)
			choice2 = input("选择进入>>:")
			if choice2 in menu[choice]:
				while True:
					pass
				pass

				#再测试！！！
				##tPest again
