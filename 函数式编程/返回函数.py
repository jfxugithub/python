#!/usr/bin/evn python3.5
# -*- coding: utf-8 -*-
'''
高阶函数除了可以将函数作为入参，还可以将函数作为返回值
'''

#eg：求和
def lazy_sum(*num):   #参数以tuple的形式导入

    def sum():
        sume = 0
        for n in num:
          sume = sume + n
        return sume
    return sum

f = lazy_sum(1,2,3);   #返回求和函数
print("1+2+3=%d" % f())             #执行求和函数

#注意：相关参数和变量都保存在返回的函数中（注意：可以引用但是不能修改外部函数的变量和参数）----闭包

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print("闭包函数测试：",f1(),f2(),f3())
#结果都是9，因为i的终值是3，所以三个函数中保存的i都是3

#注意：返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

def createCounter():
    #定义一个生成器，可以生成从1开始的所有自然数
    def get_nu():
        n=0
        while True :
            n += 1
            yield n

    it = get_nu() #获取生成器

    def counter():
        return next(it) #调用一次函数就从生成器中获取一个自然数，实现递增的效果

    return counter
print("递增函数的实现：")
f = createCounter()
for n in range(0,10):
    print(f())