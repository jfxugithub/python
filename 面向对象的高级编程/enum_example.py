#!/usr/bin/evn python
# -*- coding: utf-8 -*-

from enum import Enum,unique

##eg1:生成一个枚举实例
#枚举类型定义一个class类型，每个常量都是class的一个唯一实例
##value属性则是自动赋给成员的int常量，默认从1开始计数

Mon = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
#可以通过Month.Jan来引用常量1
for name,member in Mon.__members__.items():
    print(name,'=>',member,'=',member.value)



##eg2:定义一个更精确的枚举类

@unique        #unique 装饰器可以帮助检查没有重复值
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


#Weekday.Fri引用常量5

