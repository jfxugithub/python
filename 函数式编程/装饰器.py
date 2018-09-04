#!/usr/bin/evn python3.5
# -*- coding: utf-8 -*-
import datetime
'''
函数也是一个对象，函数对象可以赋值给一个变量，所以通过变量也可以调用函数
函数对象有一个__name__属性，显示函数的名字
'''
#eg:
print("通过变量调用函数，并显示函数名称")
def now1() :
    print("当前时间是：",datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))

f = now1;
print("由函数："+f.__name__+"()显示")
f()
#=============================================================================================#

'''
当需要增强now函数，但是又不改变now()函数的定义，在代码运行期间动态增加功能的方式 -- 装饰器(decorator)
'''

#eg:为now2()函数添加打印日志的功能
def log2(func) :
    def wrapper(*args,**kw) :
        print("call %s()" % func.__name__)
        return func(*args,**kw)
    return wrapper

@log2        #相当于执行了 now2 = log2(now2)
            #注意：log2函数必须定义在now2前面，否则会报log2未定义的错误
def now2() :
    print("当前时间是：",datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))

now2()    #调用的结果是
          #call now2()
          #当前时间是： 18-08-07 13:36:41

print("我其实是"+now2.__name__+"()")

##由于log1()是一个decorator(装饰器)，返回一个函数，所以，原来的now2()函数仍然存在，
##只是现在同名的now2变量指向了新的函数，于是调用now2()将执行新函数，
##即在log()2函数中返回的wrapper()函数。


#=============================================================================================#
#如果decorator本身需要传参，那么就需要编写一个返回decorator的高阶函数
#eg:
def log3(text) :
    def decorator(func):
        def wrapper(*args, **kw):
            print(text + " %s()" % func.__name__)
            return func(*args, **kw)

        return wrapper
    return decorator

@log3("execute")   #相当于now3 = log3("execute")(now3)
def now3() :
    print("当前时间是：",datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))

now3()
print("我其实是"+now3.__name__+"()")


#=============================================================================================#
##通过上面两个例子可以看出，通过装饰器，虽然执行的是nowx，但实际名字依然是wrapper
##这对于有些依赖函数签名的代码执行就会出错
#eg:完整的写法
import functools

def log(func):
    @functools.wraps(func)      #对内部函数的__name__属性进行修改
    def wrapper(*args, **kw):
        print("call %s()" % func.__name__)
        return func(*args, **kw)

    return wrapper
@log
def now() :
    print("当前时间是：",datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))

now()
print("我是"+now.__name__+"()")

#eg:练习(为任意一个函数计算出执行时间)
import time
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*argu,**keyargu) :
        startTime = int(round(time.time() * 1000))   #ms级时间戳
        val = fn(*argu, **keyargu)
        endTime = int(round(time.time() * 1000))
        print('%s executed in %s ms' % (fn.__name__, endTime-startTime))
        return val
    return wrapper


@metric
def fast(x, y):
    time.sleep(1)
    return x + y

print("fast(400+612) = ",fast(400,612))