# 高级特性

# 切片
# 例子：取一个list或tuple的部分元素
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']


# 取前三个元素
print(L[0:3])
# 取倒数第一个元素
print(L[-1])
print(L[-2:])
print(L[-2:-1])

# 迭代
for ch in 'ABC':
    print(ch)

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# 列表生成式
L = [x * x for x in range(1, 11)]
print(L)

L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)

L = ['Hello', 'World', 'IBM', 'Apple']
L = [s.lower() for s in L]

# 生成器
# L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator
L = [x * x for x in range(10)]
g = (x * x for x in range(10))
print(next(g))
