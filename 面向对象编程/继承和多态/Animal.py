#!/usr/bin/evn python
# -*- coding: utf-8 -*-

#############################
#定义一个父类
#############################
class Animal(object):
    def run(self):
        print('Animal is running')

#############################
#定义两个个Animal的子类
#覆盖run方法，实现多态
#############################
class Dog(Animal):
    def run(self):
        print('Dog is running')

class Cat(Animal):
    def run(self):
        print('Cat is running')

###############################
#定义一个普通方法
##############################
def run_twice(animal):
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

'''
注意，以上例程遵循了著名的《开闭原则》
    对扩展开放：允许新增Animal子类
    对修改封闭：不需要修改依赖Animal类型的run_twice()等函数
'''

'''
继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
'''

#############################
#鸭子类型
#Python是一门动态语言，即使run_twice中传入的参数不是Animal及其子类的类型，只要有run方法一样可以传入，这种类型就叫鸭子类型
#############################

class Duck(object):
    def run(self):
        print('duck is running')

run_twice(Duck())