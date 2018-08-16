#!/usr/bin/evn python
# -*- coding: utf-8 -*-
'''
    如果一个类想被用于for ... in循环，类似list或tuple那样，
就必须实现一个__iter__()方法，该方法返回一个迭代对象，
然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
直到遇到StopIteration错误时退出循环。
'''

#eg:斐波那契数列(除了前两个数以外，每个数都是前两个数的和)

class Fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    #返回一个迭代对象
    def __iter__(self):
        return self     # 实例本身就是迭代对象，故返回自己

    #重写迭代对象的next方法
    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a > 100:
            raise StopIteration
        return self.a


#通过迭代打印数列
for i in Fib():
    print(i)