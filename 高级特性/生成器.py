#!/usr/bin/evn python3.5
# -*- coding: utf-8 -*-
#生成器（generator）：一边循环一边通过算法推算出来机制
#优点：不必创建完整的list，节省大量的空间

#方法一：将列表生成式的[]改成()就创建了一个generator
#eg:

L = [ x*x for x in range(10) ] #通过列表生成式生成一个列表
print(L)
g = (x*x for x in range(10))  #生成一个generator
print(g)

#打印generator的元素
print("通过列表生成器，迭代对象")
for n in g :
    print(n)

#方法二：如果一个函数中有yield关键字，那么这个函数就是一个generator

#eg:生成斐波拉契数列(除第一个数和第二个数外，任意一个数都由前两个数相加得到)
#generator函数的执行顺序是遇到yield语句返回，再次执行时从yield语句处继续执行
def fib(n=0):
    i,a,b = 0,0,1
    while i < n:
        yield b
        a,b = b,a+b
        i = i + 1
    return None

print("斐波拉契数列")
for n in fib(10):
    print(n)

#杨辉三角定义
def triangles(n=0):
    if n == 0 :
        return
    i,j=0,1
    li = []
    while i < n :
        if i == 0 or i == 1 :
            li.append(1)     #i=0的时候生成第一行列表，i=1的时候生成第二行列表
        else:
            liTmp=[1]
            while j < len(li):
                liTmp.append(li[j-1]+li[j])
                j = j+1
            liTmp.append(1)
            li=liTmp
            j=1
        i = i + 1
        yield li

print("打印杨辉三角")
for lis in triangles(8):
    print(lis)