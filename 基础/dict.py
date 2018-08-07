#!/usr/bin/evn python3.5
# -*- coding: utf-8 -*-
'''
#dict(字典)，在Java中称为map，使用键值对存储
#特点，查找速度快，占用内存大
#dict通过提供的key值计算出对应的value的地址，所以无论元素有多少对，都可以很快找出来
#dict中key值是唯一的，不可重复的
'''
stu = {"bob":32,"lisha":99,"jack":80,"fionn":100}
print(stu)
print(stu["fionn"])

#通过get方法可以检查key值是否存在
#如果不存在，则默认返回None，也可以指定返回值
print(stu.get("jack"))
print(stu.get("dat"))
print(stu.get("dat",-1))

#获取dict的所有key值
li = list(stu.keys())
print(li)