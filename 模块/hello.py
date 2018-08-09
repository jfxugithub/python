#/usr/bin/evn python3.5
# -*- coding: utf-8 -*-

'a test module'    #任何模块代码的第一个字符串都被视为模块的文档注释,可以通过__doc__引用

__author__ = 'jfxu'

import sys

def test():
    print(__doc__)              #打印模块文档注释
    args = sys.argv             #sys.argv用list存储了所有的入参（第一个入参永远是该模块的名称：hello.pys）
    print("sys.argv:",sys.argv)
    if len(args) == 1:
        print("hello python...")
    elif len(args) == 2:
        print("hello %s" % args[1])
    else:
        print("Too many arguments!")

#当在命令行中直接使用Python3.5 hello.py 运行时，Python解析器会把特殊变量__name__赋值‘__main__’
#而在其它地方导入该模块，则该变量就不是'__main__'
#通常用于测试
if __name__ == '__main__':
    test()


'''
作用域
    1.一般函数和变量可以直接被引用
    2.类似于__doc__、__author__特殊变量，可以直接被引用但是有特殊用途
    3.类似_xx,__xx这样的函数或者变量是非公开的（private）,不应该被直接引用
注意：private变量或者函数是可以被引用的（Python无法强制限制），但是从编程习惯上来说是不应该被引用的
'''













