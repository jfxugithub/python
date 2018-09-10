#!/usr/bin/evn python
# -*- coding: utf-8 -*-

######################################################################
#__slots__：限制实例属性和方法的范围（只对当前类有效，对子类无效）
#          如果子类中也有__slots__,则动态实例属性和方法的范围是父类和子类的合集
######################################################################
class Student(object):
    __slots__ = ('name','score','get_score')     #限制动态绑定的属性和方法范围

stu = Student()
stu.name = "julia"
stu.score = 90
#stu.sex = "woman" #会报错Student no attribute 'sex'

#from types import MethodType
def get_score(self):
    return self.score

#stu.get_score = MethodType(get_score,stu)   #动态绑定方法（仅仅当前实例有效）
Student.get_score = get_score                #动态绑定方法（所有实例均可使用）
print("%s score is %d" % (stu.name,stu.get_score()))

##################################################################
class CollegeStu(Student):
    pass

cstu = CollegeStu()
cstu.school = 'HFUU'            #父类中的限制对子类无效，所以可以动态绑定school属性
cstu.name = 'alen'
print("%s school is \"%s\"" % (cstu.name,cstu.school))


#################################################################
class MiddleSchoolStu(Student):
    __slots__ = ('classs')          #子类中也做了限制，所以动态绑定属性的范围是父类和子类的合集

Mstu = MiddleSchoolStu()
Mstu.name = 'fionn'
Mstu.classs = '一班'
#Mstu.school = 'HQEZ'     #会报错Student no attribute 'school'
print('%s 的是%s的学生' % (Mstu.name,Mstu.classs))


