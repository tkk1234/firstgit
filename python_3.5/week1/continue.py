#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tkk1234
# @Date:   2018-05-11 15:25:01
# @Last Modified by:   tkk1234
# @Last Modified time: 2018-05-11 15:41:16
for x in range(1,10):
	if x < 3:
		print("loop", x)
	else:
		continue   #跳出本次循环，继续下面的语句（或循环）
	print("hehe")
