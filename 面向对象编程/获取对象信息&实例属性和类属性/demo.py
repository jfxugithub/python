#!/usr/bin/evn python
# -*- coding: utf-8 -*-

class Animal(object):
    pass

class Dog(Animal):
    pass
class Husky(Dog):
    pass
############################
#获取对象信息
#############################
'''==========================
###type()函数
###判断对象类型
============================'''

if type('123') == str:
    print('this is str')
else:
    print('this is not str')

husky = Husky()
############
####type()函数取出的是变量的直接类型
if(type(husky) == Animal):
    print("husky is Animal...")
if (type(husky) == Dog):
    print("husky is Dog...")
if(type(husky) == Husky):
    print("husky is husky...")

################################
#isinstance()函数判断数据类型
###############################
if(isinstance(husky,Animal)):
    print("husky is Animal...")

if (isinstance(husky,Dog)):
    print("husky is Dog...")

if(isinstance(husky,Husky)):
    print("husky is husky...")


############################################
#dir()--获取对象的所有属性和方法，通过list的形式返回
############################################
print("str类型的对象所有属性和方法：",dir('abc'))


###################################
#实例属性：通过实例动态定义的属性,只属于当前实例
#类属性：类中定义的属性
###################################
class Student(object):
    name=''                   #类属性
    def __init__(self,name):
        self.name = name


stu = Student('alian')
stu.score = 90                #实例属性

print("name:%s score: %d" % (stu.name,stu.score))

stu2 = Student("hong")
stu2.name = 'dong'            #当前实例属性会覆盖掉类属性，但是类属性是存在的，可以通过Student.name访问
stu2.score = 80
print("name:%s score: %d" % (stu2.name,stu2.score))


'''
####小结：

实例属性属于各个实例所有，互不干扰；

类属性属于类所有，所有实例共享一个属性；

不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
'''