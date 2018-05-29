#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tkk1234
# @Date:   2018-05-18 16:11:04
# @Last Modified by:   tkk1234
# @Last Modified time: 2018-05-18 17:40:51

# 集合是一个无序的，不重复的数据组合，它的主要作用如下：
# 去重，把一个列表变成集合，就自动去重了
# 关系测试，测试两组数据之前的交集、差集、并集等关系

list_1 = [1,4,5,7,7,8,8]  #列表
list_1 = set(list_1)  #用set把list_1变成集合，集合的特点是去重。
print(list_1,type(list_1))  #用type看一下类型，为set

list_2 = set([4,7,99,5,33]) #集合
print(list_1,list_2)   #这样打印list_1和list_2出来可以看到2个list有交集部分，比如：4，7，5

#求交集部分

print(list_1.intersection(list_2)) #求出交集为4,5,7

#求并集部分

print(list_1.union(list_2))

#求差集部分（相同部分之外的部分，即差异部分） 把list_1里面有，但list_2里面没有list_1里面的东西并打印出来
print(list_1.difference(list_2))

#求对称差集（重复的去掉，双方都没有的取出来）
print(list_1.symmetric_difference(list_2))

#求是否为子集
print(list_1.issubset(list_2))

list_3 = set([1,7,8])
print(list_3.issubset(list_1))  #因为list_3的集合都在list_1里，所以判断为True。

#求是否为父集
print(list_1.issuperset(list_2))

#求有无交集，返回true或false
print(list_1.isdisjoint(list_3))   #list_1和list_3有交集，所以返回false

#符号判断法
#求交集

print(list_1 & list_2)

#求并集
print(list_1 | list_2)

#求差集
print(list_1 - list_2) #in list_1 but not in list_2

#对称差集
print(list_1 ^ list_2)

#集合添加
list_1.add(999)
print(list_1)

#删除集合元素,并返回删了哪个（随机删除）
print(list_1.pop())

# print(list_1.remove('ddd'))  #remove如果删了不存在的元素，则会报错
print(list_1.discard(1)) #discard如果删了不存在的元素，也不会报错
