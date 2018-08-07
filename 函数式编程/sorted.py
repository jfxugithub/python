#!/usr/bin/evn python3.5
# -*- coding: utf-8 -*-
'''
sorted:对序列进行排序
'''
#eg:对list数字序列进行排序
li = [5,-2,8,3,-9,1,4]
print(sorted(li))     #默认从小到大排序

#可以通过key函数实现自定义排序
#key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
#eg:对list中的元素按照绝对值的顺序排列
print(sorted(li,key=abs))
print(sorted(li,key=abs,reverse=True))      #通过关键字reverse进行逆序排序

#提供一个dict，（名字，成绩）
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#eg:按学生名字排序
def sortedByName(stu):
    return stu[0]

print(sorted(L,key=sortedByName))

#eg:按学生成绩排序
def sortedByGrade(stu):
    return stu[1]

print(sorted(L,key=sortedByGrade))