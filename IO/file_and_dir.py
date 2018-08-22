#Python内置的os模块也可以直接调用操作系统提供的接口函数

import os
import shutil

def system_operation():
    print("这个计算机的类型是：", os.name)  ##posix --> linux unix macos ; nt --> windowns
    print("这个计算机的详细信息是：\n", os.uname())
    print("操作系统中定义的环境变量：\n", os.environ)
    print("获取某个环境变量：\n", os.environ.get("PATH"))

def path_operation():
    localPath = os.path.abspath(".")
    print("查看当前的绝对路径：\n", localPath)
    newPath = os.path.join(localPath, "test")  # 追加路径(两个路径拼接时不要用字符串直接连接，因为不同的操作系统表达路径的方式不同)
    print(newPath)
    # os.mkdir(newPath)    #创建目录
    # os.rmdir(newPath)    #删除目录
    print("拆分路径：\n", os.path.split(newPath))
    print("拆分扩展名\n", os.path.splitext("/usr/local/test.sh"))

def file_operation():
    ##文件重命名
    os.rename("/home/jfxu/Desktop/test.py.txt", "/home/jfxu/Desktop/test.py")
    ##删除文件
    os.remove("/home/jfxu/Desktop/test.py")
    ##复制文件
    '''
    os模块中没有复制的功能函数，因为复制文件并非由操作系统提供的系统调用
    shutil模块提供了copyfile()函数，这个模块可以看作是os模块的扩展模块
    '''
    ##文件的复制
    shutil.copyfile("/home/jfxu/Desktop/test.py", "/home/jfxu/Desktop/test.sh")

# system_operation()
# path_operation()
# file_operation()

def list_all(path):
    localPath = os.path.abspath(path)
    print("路径",localPath,"下的所有文件夹：\n")
    for x in os.listdir(localPath):
        print(x)

list_all("/home/jfxu")