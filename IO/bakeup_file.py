"""
输入文件路径,然后程序自动复制一份备份文件
分析:
    1.判断文件是否存在
    2.创建新文件的名字
    3.读取文件内容,存入临时变量中
    4.将读取的数据写入新文件
    5.关闭新旧文件
"""
import os


def bakup_file():
    old_file_name = input("please input file abstract path:")
    if not os.path.isfile(old_file_name):
        print("您输入的文件不存在")
        return

    file_nu = old_file_name.rfind('.')
    # 判断是否带后缀名,分别处理
    if file_nu > 0:
        new_file_name = old_file_name[:file_nu] + '.bak' + old_file_name[file_nu:]
    else:
        new_file_name = old_file_name + ".bak"

    old_file = open(old_file_name, 'r')
    new_file = open(new_file_name, 'w')

    for content in old_file.readlines():
        new_file.write(content)

    old_file.close()
    new_file.close()


# /home/jfxu/Desktop/day13笔记.md
bakup_file()
