#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tkk1234
# @Date:   2018-05-19 10:17:21
# @Last Modified by:   tkk1234
# @Last Modified time: 2018-05-25 15:39:26

# data = open("C:/Users/Administrator.USER-20170731GE/Desktop/云舞2.txt",encoding="utf-8").read()
# print(data)

# f = open("C:/Users/Administrator.USER-20170731GE/Desktop/云舞2.txt",'r',encoding="utf-8")  #打开的文件内存
# # 对象赋值一个变量，通常变量名为f。这个方法叫做文件句柄,'r'代表读模式，如果没标明默认就是读。

#写入内容（python中要么读，要么写。不能同时）：
f2 = open("C:/Users/Administrator.USER-20170731GE/Desktop/云舞2.txt",'w',encoding="utf-8")
f2.write("我爱区块链\n")
f2.write("我爱运维，哈哈哈\n")
# 'w'代表写模式，要谨慎，如果和先前的文件名不一样它会重新创建，并把内容写入其中，但如果文件名一样它会覆盖当前内容！


#然后读取内容
data2 = open("C:/Users/Administrator.USER-20170731GE/Desktop/云舞2.txt",encoding="utf-8").read()
print(data2)


#追加内容
f3 = open("C:/Users/Administrator.USER-20170731GE/Desktop/云舞2.txt",'a',encoding="utf-8")
f3.write("测试追加222\n")
f3.write("测试追加2")
f3.write("测试追加3")

# 'a' 代表追加内容
f3.close() #关闭文件

data3 = open("C:/Users/Administrator.USER-20170731GE/Desktop/云舞2.txt",encoding="utf-8").read()
print(data3)


