# 编码与字符格式
print('Hello, %s' % 'world')

print('%2d-%02d' % (3, 1))

print('%.2f' % 3.1415926)

print('ABC'.encode('ascii'))

print('中文'.encode('utf-8'))

# list 一种有序的集合，可以随时添加和删除其中的元素 []
# tuple 一旦初始化就不能修改  ()
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[-1])

classmates.append("edison")
print(classmates)

classmates.pop(1)
print(classmates)

# 条件判断
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# dict  键-值（key-value）存储
# set   一组key的集合，但不存储value。由于key不能重复
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
print('Michael' in d)

# *args是可变参数，args接收的是一个tuple；
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc(1, 2)
nums = [1, 2, 3]
calc(*nums)
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

#
# **kw是关键字参数，kw接收的是一个dict。