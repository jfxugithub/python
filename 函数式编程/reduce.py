#!/usr/bin/evn python3.5
# -*- coding: utf-8 -*-
from functools import reduce
'''
reduce 函数接收两个参数
    argu1--函数名
    argu2--iterator
result:传入的函数作用在序列上，这个函数必须接收两个参数,reduce把结果继续和序列的下一个元素做累积计算

reduce(f,[x1,x2,x3,x4]) => f(f(f(x1,x2),x3),x4)
'''

#eg:将字符串数字转换成int数字
def charToInt(cha):
    dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return dic[cha]

def func(a,b):
    return a*10+b

print(list(map(charToInt,"12345")))
print(reduce(func,map(charToInt,"12345")))
