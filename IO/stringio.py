from io import StringIO

'''
很多时候会从内存中读取IO数据
StringIO就是对内存中的str进行操作
'''

def string_io_operation():
    f = StringIO()
    f.write('hello world!')  # 写
    print(f.getvalue())  # 获得写入后的str
    f.close()
    f = StringIO('hi \n julia!\n')
    print(f.readline())  # 读
    f.close()


string_io_operation()
