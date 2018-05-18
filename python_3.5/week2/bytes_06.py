#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tkk1234
# @Date:   2018-05-14 11:41:23
# @Last Modified by:   tkk1234
# @Last Modified time: 2018-05-14 15:21:51
#把字符串转成bytes类型（bytes包含utf-8类型）
msg = "我爱北京天安门"

print(msg.encode())  #默认转换成utf-8类型
