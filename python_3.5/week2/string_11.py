#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tkk1234
# @Date:   2018-05-16 10:28:35
# @Last Modified by:   tkk1234
# @Last Modified time: 2018-05-16 15:29:01
name = "ab1234 is rich man"
name2 = "My \tname is {name} and i am {years} old"
test = "11"
print(name.title()) #首字母大写，和name.capitalize()效果也一样。
print(name.count("a")) #计算字符串中a的数量。
print(name.center(30,"-")) #包括tkk1234在内30个字符，并把tkk1234放中间 效果：------------ab1234------------
print(name.endswith("34")) #判断tkk1234是否以34结尾。例如像判断某个邮件地址是否以.com结尾就可以用到。
print(name.startswith("tk")) #道理同上。
print(name.find("i"))  #找字符索引。
print(name[name.find("i"):15])   #用find切片。name.find("i")直接查找到i的索引为7
print(name[7:15]) #效果同上面
print(name2.format(name='ab1234',years=23))  #格式化。
print(test.isalnum())  #判断是不是阿拉伯数字，不过像ab123带有数字的还会判定为 True
print('ab123'.isalnum())  #数字和英文混合也判定为true
print('aba'.isalpha()) #判断是不是全英文
print('1A'.isdecimal())  #检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。不常用
print('5'.isdigit()) #判断是否为数字，最常用。
print(' '.isspace()) #判断是否有空格。
print('My name is'.istitle()) #判断每个首字母是否为大写。
print('My Name Is'.isupper()) #判断是否全为大写
print('+'.join(['1','2','3','4','5']))  #将序列中的元素以指定的字符连接生成一个新的字符串。
print('*'.join(['1','2','3','4','5']))  #将序列中的元素以指定的字符连接生成一个新的字符串。
print('@'.join(["tkk1234","163.com"]))

s1 = "-"
s2 = ""
seq = ["r", "u", "n", "o", "o", "b"] # 字符串序列seq = ("r", "u", "n", "o", "o", "b") 元组形式也可以，待考。
print (s1.join( seq ))
print (s2.join( seq ))

print("tkk1234  ".strip()) #去左右空格
print("tkk1234".replace("4","hh")) #把tkk1234后面的4替换成hh
print("tkk1234".rfind('k'))  #找出最右边的
print("tkk1234 ll".split())  #拆分成2个元素
print("1+2+3+4".split("+")) #按+进行拆分
print("Abbbcc1234".swapcase())  #对字符串的大小写字母进行转换。
