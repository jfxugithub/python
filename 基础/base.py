#!/usr/bin/evn python3.5
# -*- coding: utf-8 -*-       #按照utf8编码读取源代码

print("hello python...")


#print("hello","word","遇到逗号会输出一个空格")

#print可以直接输出整数
'''
print("100+200=",100+200)
print("1024 * 768=",1024*768)
'''

#读取终端的输入内容
'''
print("请输入您的姓名：")
name=input()
print("你的名字是:",name)
'''

#python 每一行都代表一条语句
#当语句末尾以:结尾的时候缩进语句视为代码块
#python 区分大小写
'''
num=10
if num < 100:
    print(num)
else:
    print(num-100)
'''
#布尔值True/False
#布尔值常用于and（与）、or（或）、not（非）
#空值：Python中一个特殊的空值用None表示，不能理解为0,0是有意义的
#在Python中一个变量可以反复赋值成不同类型的数据

#变量的赋值过程
#a="abc"    #在内存中创建一个abc字符串，在内存中创建一个a的变量，并把它指向abc
#b=a        #变量之间的赋值实际上就是将b指向a所指向的内容

#Python中的除法有两种'/'结果是一个浮点数，即使两个整数可以除尽；'//':两个整数相除结果仍为一个整数（只取整数部分，不考虑除数有浮点数）

#Python的格式化输出(%s通用，可以将所有的数据转换成字符串)
#输出字符串中如果有%时，可以通过%%进行转义
#print("姓名:%s 年龄:%d 满勤率:%s%%" % ("小米",20,100))

#list/tuple
#list是一个有序集合，可以随时添加和删除内容
#占用内存少，查找速度随着元素的增加而变慢
'''
list=["hello","word",[1,2,3]]
#通过下标进行访问

print(list[0])
print(list[2][0])
print("list的长度:",len(list))    #获取list的长度
list.append("I am Python")        #在末尾追加元素
print(list[len(list)-1])
list.insert(1,"a")                #在指定位置插入元素
print(list[1])
print(list[2])
list.pop()                        #删除末尾元素
list.pop(1)                       #删除指定下标元素
print(list[len(list)-1])
print(list[1])
'''
#tuple（元祖）一经初始化后，tuple的元素不能变
#tuple和list一样可以用下标进行引用，但是因其特点所以就没有了增减元素的方法
#虽然tuple的元素不能改变，但是如果元素是一个list，其指向的内容还是可以修改的
'''
b="hello"
tu=("a",b,[1,2,3])
print(tu)

tu[0]="d"    #会报错
print(tu[0])

b="python"
print(tu[1])      #打印的依然是hello，因为初始化的时候b以及被替换成指向的字符串了

tu[2].append(4)   #tu[2]指向list这个指向没有改变，依然是同一个list，只是list改变了
print(tu[2])
'''

#dict/set（无序的）

#set
#是一组key的集合，不能有重复的值(重复的值会被过滤掉)
#要创建一个set需要一个list集合
ch = set(["a",'b','c','d','e','a'])
print(ch)
ch.add("t")
ch.remove("a")
print(ch)
#条件判断
#注意：input函数读取后返回的数据是字符串，所以需要用int()转换成整数
'''
year=input("birth(year):")
if int(year) > 2000:
    print("你是00后")
else:
    print("你是00前")
'''

#循环
#for循环
'''
li=list(range(100))    #通过range()产生0-99的整数序列，然后通过list()函数转换成list
#print(li)

sum=0
for i in li:
    sum = sum +i
print("0-99的和：",sum)
'''
#while循环
'''
li=list(range(5))
num=len(li)
multi=1
while num-1:
    multi = multi * li[num-1]
    num = num - 1;
print("1-4的乘积:",multi)
'''










