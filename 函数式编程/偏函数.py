#!/usr/bin/evn python3.5
# -*- coding: utf-8 -*-
'''
当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单
'''
import functools
#int()函数：把字符串数字转换成数字，其中有一个默认参数base=10，如果想大量转换二进制字符串，可以进行如下操作
int2 = functools.partial(int,base=2)
print("二进制转换成十进制：0011=" , int2("0011"))

#max()提取数列中最大的数字
max2 = functools.partial(max,10)      #max函数的入参是不限量的，此时偏函数有一个默认参数10，所以在运行max2时自动添加10这个数
print("10,1,2,3中最大数是：" , max2(1,2,3))