#!/usr/bin/evn python3.5
# -*- coding: utf-8 -*-

######################
#一个简单的pojo
######################
'''
class Student(object):
    __name = ''
    __score = 0
    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self, score):

        if not isinstance(score, int):
            raise ValueError('score must be an integer!')

        if score > 100 or score < 0:
            raise ValueError('the score value is out range...')
        else:
            self.__score = score

stu = Student()
stu.set_name('julia')
stu.set_score(100)
print('%s score is %d' % (stu.get_name(),stu.get_score()))
'''
#########################################################
#上面调用set的方法略显复杂
#下面的方法既能检查参数，又可以用类似属性这样简单的方式来访问类的变量
#########################################################
'''
@property的的使用：把一个getter方法变成属性，只需要加上@property就可以了，
    此时，@property本身又创建了另一个装饰器@score2.setter，负责把一个setter方法变成属性赋值，
    于是，我们就拥有一个可控的属性操作：
'''
class Student(object):

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,val):
        if not isinstance(val, int):
            raise ValueError('score must be an integer!')

        if val > 100 or val < 0:
            raise ValueError('the score value is out range...')
        else:
            self.__score = val

stu = Student()
stu.name = 'alen'
stu.score = 89
print('%s score is %d' % (stu.name,stu.score))