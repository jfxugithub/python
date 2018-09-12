#!/usr/bin/evn python3.5
# -*- coding: utf-8 -*-
'''
filter:用于过滤序列
    arg1--函数名
    arg2--序列
result：函数依次作用与序列的每个元素，然后根据函数的返回值True/False决定是否保留该元素
'''


# eg:提取列表中的偶数形成新的列表
def checkEven(n):
    return n % 2 == 0


li = list(range(1, 20))

print(list(filter(checkEven, li)))

#返回100以内的偶数
print(list(filter(lambda nu:(nu % 2 == 0), range(1, 100))))
