#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tkk1234
# @Date:   2018-05-11 11:09:34
# @Last Modified by:   tkk1234
# @Last Modified time: 2018-05-11 16:11:59
# 对了就退出，如果错3次则问是否还想继续玩？
count = 0
age = 20
while count < 3:  # 如果<3条件成立，即循环开始（有条件为真）。通俗点讲：循环执行下面的代码3次（直到猜对才停止）
    # input输入数字实际上是字符串，所以要加int转换类型。
    guess_age = int(input("pls enter my age:"))
# 是否是字符还是数字可以用print(type(guess_age))来检验
    if guess_age == age:  # 20如果不加引号代表数字，如果加了表示字符串
        print("you got it!")
        break  # 猜对了就断开
    elif guess_age > age:
        print("no")
    elif guess_age < age:
        print("no")
    count += 1
    if count == 3:
        continue_confirm = input(
            "You have tried too many times! do you want to continue? y or n?")
        if continue_confirm != 'n':
            count = 0  # 如果答案为n，则计数重置为0，重新开始循环猜年龄。
