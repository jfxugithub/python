"""
文件的定位:
    获取读取数据指针的位置
"""
import os

str = "abc\n123\nsdjfljasljdflj\nwejoweoojfn"
new_file = open("./hello", 'w')
new_file.write(str)
new_file = open("./hello", 'r')

"""==========================tell()==========================="""

new_file.read(1)
print(new_file.tell())  # 读取当前指针的位置

new_file.read(1)
print(new_file.tell())

new_file.read(1)
print(new_file.tell())

new_file.read(1)
print(new_file.tell())

new_file.read(1)
print(new_file.tell())

"""修改指针的位置"""
"""======================seek============================="""
new_file.read(1)
print(new_file.tell())

new_file.read(1)
print(new_file.tell())

new_file.seek(0)    #指针重新定位到文件初始位置

new_file.read(1)
print(new_file.tell())

new_file.read(1)
print(new_file.tell())

new_file.close()

os.rename("./hello","./hello.bak")

