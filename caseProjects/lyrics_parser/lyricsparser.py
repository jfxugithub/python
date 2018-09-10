from time import sleep


def lyrics_parser(path):
    """歌词解析器,用字典存储歌词内容以及对应的时间点,然后根据时间间隔打印歌词"""

    def show_lyrics(lyrics_list, lyrics_dict):
        pre_time = 0  # 记录上一个时间点
        for index, key_ in enumerate(lyrics_list):
            if isinstance(key_, str):  # 如果key不是时间,则直接显示,作者标题一类的内容
                print(lyrics_dict[key_])
            else:
                sleep(key_ - pre_time)  # 按照时间间隔显示歌词
                print(lyrics_dict[key_])
                pre_time = key_

    lyricsfile = open(path, 'r')
    top_dict = {}  # 存放标题名和作者等
    top_list = []
    cont_dict = {}  # 歌词内容,key用时间表示,对应的内容用value表示
    cont_list = []  # 存放时间节点,也就是cont_dict的key,因为dict是无序的,所以用list进行排序后按顺序输出
    while True:
        content = lyricsfile.readline()

        if content.isspace():  # 判断是否为空行,因为空行有一个占位符:回车符;
            continue

        if content is '':  # 判断是否到文件尾,isspace方法判断''为False
            lyricsfile.close()
            break

        content = content.strip()  # 去除两端的空格,主要是去除换行符'\n'
        if content[-1] is ']':  # 判断是否是作者或者标题等
            content = content[:len(content) - 1]  # 通过切片去除末尾的']'
            key_val = content.split(':')
            key_ = key_val[0]
            val_ = key_val[1]
            top_list.append(key_)
            top_dict[key_] = val_
        else:
            yrics_list = content.split(']')
            val_ = yrics_list[-1]
            for index, con in enumerate(yrics_list):
                if index is len(yrics_list) - 1:  # 最后一个是歌词,已经被取出来了
                    break

                time = con[1:]  # 去除首行的'['
                minute = int(time.split(':')[0])
                second = float(time.split(':')[1])
                key_ = minute * 60 + second  # 转换成秒
                cont_list.append(key_)
                cont_dict[key_] = val_

    cont_list.sort()  # 对时间进行排序
    cont_dict.update(top_dict)  # 将两个dict拼接
    # print(top_list + cont_list, cont_dict)
    show_lyrics(top_list + cont_list, cont_dict)


path_ = './海阔天空.lrc'
lyrics_parser(path_)
