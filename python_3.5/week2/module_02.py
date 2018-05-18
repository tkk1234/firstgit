#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tkk1234
# @Date:   2018-05-11 16:24:28
# @Last Modified by:   tkk1234
# @Last Modified time: 2018-05-14 11:40:52
import sys  #导入自带的sys库
print(sys.argv)  #传参

import os
#cmd = os.system("dir") #调用windows系统命令 dir，但只执行命令，不保存结果，只是屏幕打印出来。
cmd = os.popen("dir").read() #真正调用windows系统命令"dir"要用这个（如果后面不加read,则只调用内存地址，还是无法显示，所以要用read读取一下这个内存地址里的内容）
print(cmd)

os.mkdir("new_dir") #直接创建文件夹名为“new_dir”  time:30:16
