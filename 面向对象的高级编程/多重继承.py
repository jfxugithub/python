#!/usr/bin/evn python3.5
# -*- coding: utf-8 -*-
#################################
#和java不同的是Python是可以多重继承的
#################################

class Animal(object):
    type = 'animal'

class Runable(object):
    def run(self):
        print('I can run...')

class Dog(Animal,Runable):
    def __init__(self):
        self.type = 'dog'

dog = Dog()
print("I am a",dog.type)
dog.run()

'''
小结：
    我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类
'''