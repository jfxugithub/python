#!/usr/bin/evn python
# -*- coding: utf-8 -*-

'''
    如果调用一个类中不存在的属性的时候，一般会直接报错
但是Python提供了一个特殊的函数__getattr__，自动返回一个属性
'''

class Student(object):
    def __init__(self,name):
        self.name = name

    def __getattr__(self, item):
        if item == 'score':
            return 99

stu = Student('alan')
print(stu.name + '成绩是:' ,stu.score)  #调用stu.score的时候，Python解释器会试图调用__getattr__来尝试获得属性值

########################
#eg:动态生成一个url
########################
class create_url(object):

    def __init__(self,path = ''):
        self.__path = path

    def __getattr__(self, item):
        return create_url(self.__path +'/' + item)  #通过递归自动生成一个URL

    def __str__(self):
        return self.__path

    __repr__ = __str__


url = create_url().home.jfxu.Document
print(url)