#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tkk1234
# @Date:   2018-05-29 16:20:10
# @Last Modified by:   tkk1234
# @Last Modified time: 2018-05-29 17:22:08
with open("C:/Users/Administrator.USER-20170731GE/Desktop/云舞2.txt",'r',encoding = "utf-8") as f:

	for line in f: # line这个英文随意写，写成ok都可以。
		print(line)

# with语句作用：
# 为了避免打开文件后忘记关闭，可以通过管理上下文，即：
# with open('log','r') as f:
# 如此方式，当with代码块执行完毕时，内部会自动关闭并释放文件（内存）资源。
# 在Python 2.7 后，with又支持同时对多个文件的上下文进行管理，即：
# with open('log1') as f, \
#		 open('log2') as f1:
#	for line in f:
#	print(line)
# 	for line in f1:
# 	print(line)


