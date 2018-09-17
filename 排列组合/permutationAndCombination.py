import itertools

##取两个字符进行两两排列
str = '0123456789abcdefghijklmnopqrstuvwxyz'
# result01 = itertools.permutations(str, 2)
# print(list(result01))

###组合
#在字符串中3 3 组合
result02 = itertools.combinations('asdfghj',3)
print(list(result02))

