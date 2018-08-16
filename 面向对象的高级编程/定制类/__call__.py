#!/usr/bin/evn python
# -*- coding: utf-8 -*-

'''
当生成一个类的实例的时候，调用类中的方法通常是：instanse.method()这种形式，
如果类中有__call__函数，则可以直接调用：instance()，执行__call__函数中的code
'''

class Student(object):
    def __init__(self,name):
        self._name = name

    def __call__(self, *args, **kwargs):
        print("我是" + self._name)

stu = Student('Fly')
stu()        #调用__call__内的代码