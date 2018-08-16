#!/usr/bin/evn python3.5
# -*- coding: utf-8 -*-


################使用特殊函数定制类########################

#########__str__#########
'''
class Student(object):

    def __init__(self,name):
        self.name = name

stu1 = Student('julia')
print(stu1)     #打印结果：<__main__.Student object at 0x7f0cf2857550>

'''

class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Student name is %s' % self.name

stu1 = Student('julia')
print(stu1)       #打印结果：Student name is julia

'''
问题：在终端中如果不调用print打印stu1，而是直接输入stu1然后回车，输出的结果仍然是：<__main__.Student object at 0x7f0cf2857550>

答案：这是因为直接显示变量调用的不是__str__()，而是__repr__()，
     两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，
     也就是说，__repr__()是为调试服务的。
     
解决方案：在类中重新定义一个__repr__()函数，也可以简单使用'__repr__ = __str__'来处理
    
'''