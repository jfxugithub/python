"""
Exception:
    当Python解释器检测到错误的时候将停止执行 -->异常
"""
import os
import sys

from django.test.utils import override_script_prefix

'''
捕获异常:
    try:
        可能会报错的代码
    except (Error1,Error2...):       #元祖中放置的是需要捕获的错误类型,也可以直接写Exception,包含所有异常
        异常处理代码
    finally:
        无论是否抛出错误都会执行的代码
'''
j = 0
try:
    a = 20 / j
except ZeroDivisionError as error_info:
    print("第%s行: %s" % (sys._getframe().f_lineno, error_info))
finally:
    print(j)

"""=================嵌套的使用=================="""
"""
eg:
    打开一个文件,读取文件内容
    创建一个文件夹,把读取的文件内容保存在新建文件夹中
    删除原来的文件只保留复制之后的文件
    关闭流
"""
try:
    old_file = open('./IO/hello', "r")  # 不知道是否存在
    content = old_file.read()

    try:
        os.mkdir('/home/jfxu/Desktop/hello')  # 不知道是否存在
    except FileExistsError as err_info:
        print(err_info)

    new_file = open('/home/jfxu/Desktop/hello/hello.txt', 'w')
    new_file.write(content)
    os.remove('./IO/hello')
    old_file.close()
    new_file.close()
except FileNotFoundError as err_info:
    print(err_info)

"""==============自定义异常=================="""


##当解释器提供的异常无法满足需求时还可以自定义
#检查输入的长度
class ShortInputException(Exception):
    def __init__(self, length, atleast):
        self.length = length   #输入数据的长度
        self.atleast = atleast #最短的长度


def main():
    content = input("请输入一个不小于100的数字:")
    try:
        if len(content) < 3:
            raise ShortInputException(len(content),3)  #人为抛出异常
    except ShortInputException as msg:
        print("最短长度是%d,输入的长度是%d",(msg.atleast,msg.length))

main()