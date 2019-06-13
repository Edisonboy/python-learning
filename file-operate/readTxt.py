filename = 'C:\\Users\\ediso\\git\\python-learning\\file-operate\\read.txt'
# file = open('兼职模特联系方式.txt', 'r')

with open(filename) as file_object:
    # file_object.read()  # 读取所有
    # file_object.readline() 读取一行
    lines = file_object.readlines() # 读取所有行
    for line in lines:
        print("=== %s" % line)
        