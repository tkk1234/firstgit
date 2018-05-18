#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tkk1234
# @Date:   2018-05-14 13:54:22
# @Last Modified by:   tkk1234
# @Last Modified time: 2018-05-15 14:59:59
names = ["test1", "test2", "test3", "test4", "test5"]
names1 = []


#增
names.append("test6")  #直接追加至names中，默认加在后面。
print(names)

names.insert(1,"haha")  #想在哪个地方插入就写哪个下标位置,例如，想在test2之前插入“haha”，直接写test2的下标位置1，然后再写插入的内容即可。
print(names)

names.insert(4,"nono")
print(names)


#删
names.remove("test5") #或del names[-1]  或names.pop()，pop后面不加下标位置默认删最后一个。也可以指示某个下标names.pop(1)
#删除整个names可以写成：del names
print(names)


#改
names[2] = "modify"
print(names)  #将2的位置改为“modify”

#查
print(names1)  #打印names1的空列表
print(names[0])
print(names[1:3]) #切片（左闭右开）
print(names[-1])
print(names[-2])
print(names[-2:])  #取后面2个连续的一定要加冒号 ：
print(names[0:3])
print(names[:3])  #如果前面是0，可以省略。

#计数
print(names.count("test1"))

#取反
names.reverse() #一定要写成这种形式 如果直接写成 print(names.reverse()) 无法正确显示结果。
print(names)

#清空列表
names.clear()
print(names)

#按字母顺序排列
names.sort()
print(names)

#并入
kk = ["jj", "ii"]
nono = [1,2,3,4,5]
kk.extend(nono)  #将nono的元素并入kk
print(kk)

#复制(待研究，未完全吃透)
ll = ["qq", "ww", "ee",["gogo", "jack"], "rr"] #列表中嵌套列表，gogo和jack被看做是一个元素。
mm = ll.copy()
print(mm)
print(ll)

ll[0] = "test"
ll[3][0] = "tkk1234"   #将列表中的嵌套元素gogo改为tkk1234, 下标3为["gogo", "jack"]的位置，下标0为gogo的位置。
print(mm)  #在更改ll[0]变量值的情况下，mm的copy值变为了 ['test', 'ww', 'ee', ['tkk1234', 'jack'], 'rr']
print(ll)

