#!/usr/bin/evn python3.5
# -*- coding: utf-8 -*-
import math      #调用math包

#定义一个处理二元一次方程的函数
def quadratic(a,b,c):
    #判断入参类型是否正确
    if not isinstance(a,(int,float)):
        raise TypeError("the argument a is err...")    #手动抛出异常
    if not isinstance(b,(int,float)):
        raise TypeError("the argument b is err...")
    if not isinstance(c,(int,float)):
        raise TypeError("the argument c is err...")

    flag = b*b - 4*a*c
    if (flag) < 0:
        print("方程无解")
        return None

    result = math.sqrt(flag)/2
    return result,-result
'''
n1 = int(input("请输入第一个参数:"));
n2 = int(input("请输入第二个参数:"));
n3 = int(input("请输入第三个参数:"));
'''
n1 = 2
n2 = 5
n3 = 3
#调用函数，返回值看起来是个多值，其实返回的是一个tuple集合（tuple可以省略括号）
re = quadratic(n1,n2,n3)  #也可以使用两个变量接受数值

#将re转换成布尔值，判断方程是否有解
if bool(re):
    print(re)

###Python函数的各种参数

#位置参数（即：必选参数，这个没有什么好说的，和其它编程语言相同）
#默认参数：可以为参数设定一个默认值，如果没有参数传递进来时，则使用默认值
#注意：使用默认参数的时候指向一定要是不变对象（如果是可变对象，在每次调用的时候有可能默认的值就会发生变化）
#eg:计算x的n次方值
def power(x,n=2):
    res = 1
    while n > 0 :
        res = res * x
        n = n - 1
    return res

print("5的平方值：",power(5))       #使用参数的默认值
print("5的三次方值：",power(5,3))

#可变参数（参数的前面加一个×，以tuple的形式导入）

#eg:定义一个求和函数
def calc(*arg) :    #参数以tuple的形式导入
    sum = 0
    for n in arg :
        sum = sum + n
    return sum

print("calc(0):",calc(0))
print("calc(5,6,7):",calc(5,6,7))

#如果已经有一个list或者tuple,将list和tuple内部元素作为可变参数传入，前面加一个×即可
li = [1,2,3]
print("li=[1,2,3],calc(*li):",calc(*li))

#关键字参数（参数前面加××，以dict的形式导入）

def person(name,age,**other):
    print("姓名：%s,年龄:%d" % (name,age))
    if bool(other):
        print("other:",other)

person("小米",16)

#递归函数

#eg:求阶乘
def recursion(n=1):
    if n == 1 :
        return 1
    return n * recursion(n-1)

print(recursion(10))

#使用递归函数需要防止栈的溢出，因为函数的调用是通过栈（stack）这种数据结构实现的，调用一次函数就会占用一个栈帧，每当函数返回就会减少一个栈帧
#上面的函数很容易出现栈的溢出如recurision(1000)
#解决方法是使用尾递归优化：函数返回的时候调用函数本身，且return语句中不能含有表达式，这样编译器或者解释器就可以给尾递归做优化，无论递归调用多少次都只占用一个栈帧

#避免栈的溢出
def recursion2(n=1,res=1):
    if n == 1:
       return res
    return recursion2(n-1,n*res)


print(recursion2(100))

#eg:解决汉诺塔问题
#思路：移动n个，要先把n-1个移动到b上，然后最后一个移动到c上，最后把b上的都移动到c上
def mov(n,a,b,c):
    if n == 1:
        print("%s --> %s" % (a,c))
    else:
        mov(n-1,a,c,b)
        mov(1,a,b,c)
        mov(n-1,b,a,c)

mov(4,"a","b","c")


