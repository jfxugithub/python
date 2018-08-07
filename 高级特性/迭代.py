#!/usr/bin/evn python3.5
# -*- coding: utf-8 -*-
#python 通过 for ... in ... 进行迭代
#可以进行迭代的有list、tuple、dict、字符串
from collections import Iterable
#eg:字符串迭代
str = "abcdefg"
for str2 in str:
    print(str2)

#eg:list迭代
li = [1,2,3,4,5,6,7,8]
for list in li[:5:2]:
    print(list)

#eg:tuple迭代
tu = (11,12,13,14,15,16)
for tup in tu[-5:]:
    print(tup)

#eg:dict迭代
#默认只迭代key
dic = {"c":3,"b":2,"a":1}
for key in dic:
    print(key)

#dict迭代value
for val in dic.values():
    print(val)

#dict同时迭代key和value
for key,val in dic.items():
    print("%s:%d" % (key,val))

#判断数据是否可以进行迭代（通过collections中的iterable来判断）
print(isinstance("abc",Iterable))
print(isinstance(123,Iterable))

#eg:查找list中的最大最小值并返回
def findMaxAndMin(li=[0,0]) :
    min=li[0]
    max=li[1]
    for num in li :
        if not isinstance(num,(int,float)):
            raise TypeError("the list data is not the int or float")
        if num < min :
            min = num
        if num > max :
            max = num

    return (min,max)

testList = [2,1,3,9,5,0,3,5,8]
print(findMaxAndMin(testList))
