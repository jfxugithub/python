#!/usr/bin/evn python3.5
# -*- coding: utf-8 -*-

#匿名函数访问每一个生成的0-9序列，将结果组合成一个list
print("匿名函数的使用：")
print("求取0-9的平方list：",list(map(lambda x:x*x,list(range(0,10)))))

'''
匿名函数的语法：
    lambda 参数：表达式   #（表达式中的变量必须是参数中的，且表达式只能有一个）
lambda:表示匿名函数的关键字
x     ：表示入参
x*x   :表示表达式

'''
#匿名函数也可以作为返回值赋值给变量
is_odd = lambda n : n % 2 == 1
print("匿名函数作为返回值的使用：")
print("提取0-10之间的奇数：",list(filter(is_odd,list(range(0,10)))))
