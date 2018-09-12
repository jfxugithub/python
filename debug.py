"""
断言:
    asset 判断条件,提示信息
    如果不满足判断条件就会报错
"""
import logging
import pdb


def get_num(nu):
    assert nu != 0, 'nu 不能等于0'
    return 10 / nu


# get_num(0)

print("=" * 30)
"""
logging
"""

logging.basicConfig(level=logging.INFO)

for i in range(10):
    logging.info(i)

print("=" * 30)

"""
pdb:python 自带模块
"""


def add_(a, b):
    j=0
    i=2
    return a + b

def demo1(a,b):
    pdb.set_trace()
    sum = add_(a,b)
    sum /=2
    return sum

# print(demo1(4,6))