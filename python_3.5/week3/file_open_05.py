#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tkk1234
# @Date:   2018-05-23 17:33:08
# @Last Modified by:   tkk1234
# @Last Modified time: 2018-05-24 17:38:20
f = open("C:/Users/Administrator.USER-20170731GE/Desktop/云舞2.txt",'r',encoding="utf-8")

#读取前2行
# for x in range(2):
# 	print(f.readline())

#打印所有行
# for line in f.readlines():
# 	print(line.strip()) #strip是去除左右空格

#取出每行下标？再做判断（低效）
# for index,line in enumerate(f.readlines()):
# 	if index == 2:
# 		print('-----我是分割线------')
# 		continue
# 	print(line.strip())

#高效的循环方法
# count = 0
# for line in f:
# 	if count == 2: #内容只有2行
# 		print('---分割线---')
# 		count += 1
# 		continue
# 	print(line)
# 	count += 1

#f.tell()指出目前内存指针位置
print(f.tell())
print(f.readline())
print(f.readline())
# 上面2个readline代表读了2行（云舞2.txt内容就2行）
print(f.tell())

f.seek(0)  #回到起始位置
print(f.readline())
print(f.tell())

#打印当前文件编码
print(f.encoding)
#不经过内存直接刷入硬盘 19:00
f1 = open("C:/Users/Administrator.USER-20170731GE/Desktop/云舞2.txt",'w',encoding="utf-8")
f1.write("Hello\n")
f1.write("hahahha\n")
f1.write("nononono\n")
f1.write("yesyesyes\n")
f1.flush()


#进度条
import sys,time
for x in range(20):
	sys.stdout.write("#")
	sys.stdout.flush()
	time.sleep(0.1)  #井号间的时间间隔

# #截断(从头开始截)
f1 = open("C:/Users/Administrator.USER-20170731GE/Desktop/云舞2.txt",'a',encoding="utf-8")  #记住模式是append，'a'
f1.truncate(2)

# f1 = open("C:/Users/Administrator.USER-20170731GE/Desktop/云舞2.txt",'r+',encoding="utf-8")  # r+ 为读写
# f1 = open("C:/Users/Administrator.USER-20170731GE/Desktop/云舞2.txt",'w+',encoding="utf-8")  # w+ 为写读
