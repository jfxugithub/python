#!/usr/bin/evn python3.5
# -*- coding: utf-8 -*-
'''
map函数接收两个参数：
    argu1--函数名
    argu2--iterable
result:map函数将传入的函数作用在序列上，产生的返回值组成一个iterator返回
'''

#eg:字符list转换成数字list
def charNuToIntNu(charNu):
    dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return dic[charNu]

li = list(map(charNuToIntNu,"123"))  #因为返回的是一个iterator，所以使用list函数转换成iteratable
print(li)


