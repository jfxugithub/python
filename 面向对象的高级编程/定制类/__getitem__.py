#!/usr/bin/evn python
# -*- coding: utf-8 -*-

############__getitem_#############
#eg:斐波那契数列(除了前两个数以外，每个数都是前两个数的和)

class Fib(object):
    def __init__(self):
        self.a = 1
        self.b = 1

    def creat_fib(self,start,stop,step=1):
        self.a = self.b = 1
        L = []
        for x in range(start):
            self.a, self.b = self.b, self.a + self.b

        L.append(self.a)
        for x in range(start,stop):
            self.a, self.b = self.b, self.a + self.b
            L.append(self.a)

        return L

    def __getitem__(self,item):    #使对象可以用下标进行索引

        if isinstance(item,int):
            return self.creat_fib(item,0)

        if isinstance(item,slice):    #如果是切片
            if isinstance(item.start,int) and isinstance(item.stop,int):
                return self.creat_fib(item.start, item.stop)

            elif item.start == None and isinstance(item.stop,int):
                return self.creat_fib(0, item.stop)

            else:
                print("the argument is error...")
                return None




f = Fib()
print('斐波那契数列第100位数是：',f[10])     #可以像list一样用下标索引

print('斐波那契数列第3-10的数列是：',f[3:10]) #list的切片效果

'''
与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
'''

