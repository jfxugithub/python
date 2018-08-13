#!/usr/bin/evn python
# -*- coding: utf-8 -*-
#########################################################
#类的定义方式如下：
#   关键字 类名(继承对象名)：
#        pass
#如果没有具体的继承对象就填写object，这是所有的类最终都会继承的类
###################################################
'''
class Student(object):
    name = ''
    age = 0
    sex = ''
    score=0
    def __init__(self , name,sex,age,score):      #相当于java中的构造器(但必须是__init__这个特殊函数)，self参数不用传入，代表当前实例
        self.name = name
        self.sex = sex
        self.age = age
        self.score = score

    def print_stu_info(self):              #定义一个类方法
        print('姓名：', self.name)
        print('年龄：', self.age)
        print('性别：', self.sex)
        print('成绩：', self.score)

stu = Student('julia','woman',10,89)
print('通过对象Student创建实例:')
stu.print_stu_info()


'''
######################################################
#访问限制
#Python中'__var'形式的变量就代表着私有变量（private）
#下例中相当于java中的pojo
######################################################
class Student(object):
    __name = ''
    __score = 0

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_score(self):
        return self.__score
    def set_score(self,score):
        self.__score = score

    def print_stu_info(self):
        print('%s 成绩是：%s' % (self.__name,self.__score))

print('访问控制：')
stu = Student()
stu.set_name('julia')
stu.set_score(100)
print(stu.get_name())
print(stu.get_score())
stu.print_stu_info()
'''
需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，

一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

双下划线开头的实例变量实际上也可以从外部访问，只是Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
'''