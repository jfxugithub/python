#!/usr/bin/evn python3.5
# -*- coding: utf-8 -*-
#对字符串切片
str="abcdef"
print(str[0:3])   #取前三个字符
print(str[:2])    #0可以默认不写
print(str[-2:])   #可以从尾部切片,同样切到尾部可以不写
print(str[1::2])  #从第一个字符开始取，且步长是2，切到尾部

#同样特性的有list、tuple，只是切完之后返回的数据依然是list、tuple类型的数据
li=[1,2,3,4,5,6,7]
print(li[3::3])
tu=(1,2,3,4,5,6,7,8,9)
print(tu[1:8:4])