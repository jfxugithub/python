import itertools
import time

START_TIME = time.time()
result_01 = itertools.product('123456', repeat=4)
# print(list(result_01))
for i in list(result_01):
    passwd = ''.join(i)
    if passwd == '3333':
        END_TIME = time.time()
        time_show = END_TIME - START_TIME
        print('密码已经找到了:%s\n使用时间:%ss' % (passwd, time_show))




########################################################
# 小名捡到一张一行卡，卡内余额100000000，
# 主人已经进去啦，出不来啦，没人知道这张卡(偷偷告诉你密码是666666)
# 假设一月30天，每天坚持去ATM尝试破解密码，每天可以尝试3次，超过3次会锁死，
# 问：多长时间能破解掉，用年月日表示结果

all_code = itertools.product('9876543210', repeat=6)
date_num = 1
flag = 0
for passwd in list(all_code):
    passwd = ''.join(passwd)
    if passwd == '666666':
        break
    flag += 1
    if flag == 3:
        flag = 0
        date_num += 1

year = 0
month = date_num // 30
day = date_num % 30
if month > 12:
    year = month // 12
    month = month % 12

print("小明花了%d-%d-%d破解了密码" % (year,month,day))
