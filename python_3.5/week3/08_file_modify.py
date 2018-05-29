#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tkk1234
# @Date:   2018-05-25 14:37:58
# @Last Modified by:   tkk1234
# @Last Modified time: 2018-05-29 17:10:51
f = open("C:/Users/Administrator.USER-20170731GE/Desktop/云舞2.txt",'r',encoding="utf-8")
f_new = open("C:/Users/Administrator.USER-20170731GE/Desktop/云舞2.bak.txt",'w',encoding="utf-8")

for line in f:
	if "我年少轻狂" in line:  #如果在line中发现“我年少轻狂”这句话
		line = line.replace("我年少轻狂","哈哈哈")  #把“我年少轻狂”改为“哈哈哈”并赋值给line
	f_new.write(line) #再把line的新内容写入f_new中
f.close()  #关闭f，为了释放内存资源
f_new.close()  #关闭f_new，为了释放内存资源

