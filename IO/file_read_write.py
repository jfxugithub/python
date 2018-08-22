######创建文件
file_path = '/home/jfxu/Desktop/test.txt'
create_mode = 'w'              #写模式打开的一种，如果文件不存在则直接 创建该文件

# f = open(file_path,read_mode)
# f.close()                    #不用文件时关闭是必须的，不解释

#另外一种写法(会在with语句结束后自动关闭文件，常用与写操作)
with open(file_path,create_mode) as f:
    pass

######写文件
'''
写模式：
     w -- 覆盖文件原先内容写操作
     a -- 在原来文件的基础上写操作
'''
write_mode = 'a'
with open(file_path,write_mode) as f:
    f.write('hi julia! ')
    f.write('I love you!')

write_mode = 'w'
with open(file_path,write_mode) as f:
    f.write('I ignore these...')

################读文件
read_mode = 'r'    #读模式打开
with open(file_path,read_mode) as f:
    while True :
        buf = f.readline()          #读取一行
        if len(buf) == 0 :
            print('read over.')
            break
        print(buf)

#################默认创建、写、读的文件的编码模式是utf-8,如果编码模式不是utf-8，则需要传入encoding参数,如GBK编码文件：
'''
 with open(file_path,read_mode,encoding='gbk') as f:
     pass
'''
# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
# 遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
'''
    f = open(file_path,read_mode, encoding='gbk', errors='ignore')
'''


