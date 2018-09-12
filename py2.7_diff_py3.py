"""
1.print 函数被print()取代
2.脚本开头不需要声明编码模式为utf-8,py3默认为utf-8编码模式
3.除法运算'/',py2中得到的是整数,py3中得到的是浮点数(py3中"//"代表整除)
4.异常中的定义别名不同
    py2:
        except exc,var
    py3:
        except exc as var
5.py2中的xrange()被py3中的range()替换
6.八进制表示方法
    py2:以0开头
    py3:以0o开头
7.不等运算符
    py2:<>
    py3:!=
8.py3舍弃了``(反引号)的用法,只能使用repr() (py2中`` ==> repr)
9.多个模块被改名
    _winreg        -->    winreg
    ConfigParser   -->    configparser
    copy_reg       -->    copyreg
    Queue          -->    queue
    SocketServer   -->    socketserver
    repr           -->    reprlib

    StringIO模块现在被合并到新的io模组内。 new, md5, gopherlib等模块被删除。 Python 2.6已经支援新的io模组。
    httplib, BaseHTTPServer, CGIHTTPServer, SimpleHTTPServer, Cookie, cookielib被合并到http包内。
    取消了exec语句，只剩下exec()函数。 Python 2.6已经支援exec()函数。
10.py3 去除了long类型,新增bytes类型
11.py3打开文件的方法已经去除了file(..)的方法
12.raw_input() 在py3中替换成input()
"""