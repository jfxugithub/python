def create_thesaurus(path):
    dict_file = open(path, 'r', encoding='utf-8')
    word_dict = {}
    content = dict_file.readlines()
    for con in content:
        key_val_list = con.split('\t')
        key = key_val_list[0].strip()
        val = key_val_list[1].strip()
        val = val.replace('\\n','\n')  #因为从文件中读取\n的时候把\n当成了字符串,自动转换成了\\n的存在,所以这里做一次还原
        word_dict[key] = val
    dict_file.close()
    return word_dict


thesaurus = create_thesaurus('./dict.txt')


def translate(words):
    if words in thesaurus.keys():
        return thesaurus[words]
    else:
        return ("%s还未收录,敬请期待!" % words)
