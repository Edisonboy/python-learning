# 高阶函数
from functools import reduce
# map/reduce
def f(x):
    return x * x
r = map(f, [1,2,3,4])
a = list(r)
print(a)


def add(x,y):
    return x + y
b = reduce(add, [1,3,5,7])
print(b)


def fn(x, y):
    return x * 10 + y

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
c = map(char2num, '13579')
c = list(c)
print(c)
reduce(fn, map(char2num, '13579'))

# filter