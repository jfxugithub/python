"""
[]      匹配[]中列举的字符(代表一个字符)
\d      可以匹配一个数字
\D      匹配非数字
\w      可以匹配一个字母,数字,下划线
\W      匹配非字符
\s      可以匹配一个空格（也包括tab等空白符）
\S      匹配非空格
.       可以匹配任意一个字符
*       表示任意多个字符（包括0个）
+       表示至少一个字符
？      表示0个或一个字符
{n}     表示n个字符
{n,}    表示至少n个字符
{n,m}   表示n-m个字符
\b      匹配字间,用的少,需要网上查
"""
#####example
# \d{3}\s+\d{3,8}
# 从左到右，匹配3个数字，至少一个空白符，3-8个数字
# eg:"101  23456"
import re

"""
[0-9a-zA-Z\_]         表示范围(可以匹配一个数字、字母或者下划线)
A|B                   可以匹配A或者B
^                     表示 行开头：^\d -->必须以数字开头
$                     表示结束：\d$ -->必须以数字结尾


"""
####python 的字符串前面加一个r代表字符串中不需要转义字符
s = "ABC\\_001"  # 双斜杠被转义成单斜杠
print(s)
s = r"ABC\\_001"  # 双斜杠正常输出
print(s)

"""========python 中re模块包含了所有正则表达式的功能============"""
##########################################匹配
# re.match(r"正则表达式",字符串)
# 如果匹配返回一个match对象，否则返回None
print('*' * 30)
s = "123_4567"
print(re.match(r'^\d{3}\_\d{3,8}$', s))

###########################################用于split()切分字符串
s = 'a,b  ,c ,d   , r'
print(s.split(","))  # 无法识别连续的空格
# 结果：['a', 'b  ', 'c ', 'd   ', ' r']
s = 'a,b  ,c ,d   , r'
print(re.split(r"[\s\,]+", s))  # 正则表达式匹配空格和逗号（至少一个）

##############################################用于分组
# 注意用()可以进行分组
s = "010-1234"
matchE = re.match(r"^(\d{3})-(\d+$)", s)

print(matchE.group(0))
print(matchE.group(1))
print(matchE.group(2))
print(matchE.group())

#######检查邮箱
email = 'jinzhengen@qq.com'
pat = '^[0-9a-zA-Z]{4,20}@[0-9a-zA-Z]{2,10}[.][com]{3}$'
result_01 = re.match(pat, email)
if result_01 is not None:
    print(result_01.group())
else:
    print(None)

############检查手机号
phone_nu = '13802507347'
pat = '^1[3-9]\d{9}$'
result_02 = re.match(pat, phone_nu)
if result_02 is not None:
    print(result_02.group())
else:
    print(None)

####re模块的高级使用
str = 'life is   short, i use python!'
#以' '或者以' ,'或者以', '进行分组
res = re.split(r",?\s+,?",str)
print(res)                #['life', 'is', 'short', 'i', 'use', 'python!']

# 查找所有能匹配到的字符/字符串
res = re.findall('\S+o\S+', str)
print(res)                #['short', 'python!']

#对正则表达式匹配到的字符进行替换/修改
print('*'*20)
res = re.sub(r'\s+','_',str,2)   #参数:正则表达式:要被替换成的字符/字符串:被操作的字符串:匹配个数(不写默认为全部)
print(res)              #life_is_short, i use python!

res = re.subn(r'\s+','_',str)
print(res)               #('life_is_short, i use python!', 5)  元祖中的5是被替换的次数