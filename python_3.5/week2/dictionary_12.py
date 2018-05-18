#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tkk1234
# @Date:   2018-05-16 15:34:12
# @Last Modified by:   tkk1234
# @Last Modified time: 2018-05-17 11:31:13
info = {
	'1':"a",
	'2':"b",
	'3':"c",
}

print(info["1"]) #取1的值
info["1"] = "tkk" #有键 “1” 的情况下，取代原先的值a，改为tkk
info["8"] = "ykk" #没有键 “8”的情况下，自动创建键和值
print(info)


#删除，del，del是python通用用法，不光对字典，列表都有用
del info["1"] #删除1的键值，info.pop["1"]也可以
print(info)


#查找字典的“键值”是否存在，并返回结果。

print(info.get('1')) #因为上面del info["1"]把 键1删除了，所以结果显示为none，即不存在
print(info.get('2')) #2的键存在，所以显示了2的值

#判断字典里有没有数据
print('1' in info)
print('2' in info)


print(info.keys()) #直接打印info的键
print(info.values()) #直接打印info的值

#字典的嵌套（嵌套的英语: nesting）
dic_nesting = {
	"a":{
	"qq":["testing", "testing1"],
	"aa":["testing3", "list_07.py"],
	"cc":["shopping_cart_10.py", "bytes_06.py"],
	},

	"b":{
	"vv":["hhhh", "ttttt"],
	"ww":["dddd", "aaaa"],
	},
}

dic_nesting["a"]["qq"][1] = "sss" #修改a键,qq子键中的位于下标1位置的（testing1）的值为sss
print(dic_nesting)

#循环
for x in info:
	print(x,info[x]) #打印键和值


