'''
BytesIO 对内存中的二进制数据进行操作
'''

from io import   BytesIO


def bytes_io_operation():
    f = BytesIO()
    f.write('你好'.encode('utf-8'))  # 请注意，写入的不是str，而是经过UTF-8编码的bytes。
    print(f.getvalue())
    f.close()
    f = BytesIO(b'\xe4\xbd\xa0\xe5\xa5\xbd')
    print(f.read())
    f.close()


bytes_io_operation()