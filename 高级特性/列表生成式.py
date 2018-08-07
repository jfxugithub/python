#!/usr/bin/evn python3.5
# -*- coding: utf-8 -*-
import os
#生成从10到30的list
li = list(range(10,31))
print(li)

#通过表达式生成list
#取1到10偶数的平方
li = [x*x for x in range(1,11) if x % 2 == 0]
print(li)

li = [m+n for m in "ABC" for n in "XYZ"]
print(li)

li = [d for d in os.listdir('/')]
print(li)

#eg:将list中的字母转换成小写字母
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [ s.lower() for s in L1 if isinstance(s,str)]
print(L2)