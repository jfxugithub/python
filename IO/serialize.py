'''
序列化:变量从内存中变成可存储或传输的过程

在不同的语言中传递对象最佳的选择是把对象序列化成json格式
    因为json表现出来的就是一个字符串，可以被所有的语言读取

    json类型                        Python类型
      {}                               dict
      []                               list
    "string"                           str
      1234.56                          int/float
    true/false                         True/False
      null                             None

python  内置的json模块提供了非常完善的Python对象到json格式的转换
'''

import json

d = dict(name='julia', age=1, score=5.0)
filePath = "/home/jfxu/Desktop/test"
with open(filePath, 'w') as f:
    json.dump(d, f)  # 将dict数据序列化成 json格式并保存到指定的文件中
with open(filePath, 'r') as f:
    buf = f.readline()
    print(buf)
    di = json.loads(buf)  # json反序列化
    print(di)



