import os
import time

def initScrip():
    readFilename = 'C:\\Users\\ediso\\Desktop\\province-raw.txt'
    writeFilename = 'C:\\Users\\ediso\\Desktop\\province-ripe.txt'

    read = open(readFilename, 'r')
    lines = read.readlines() # 读取所有行
    template = "db.cdt_shop_point.update({shopId:%s},{$set:{provinceId: NumberInt(%s), cityId: NumberInt(%s), areaId: NumberInt(%s)}},{multi:true});"
    print(len(lines))
    with open(writeFilename, 'a') as write:
        for line in lines:
            print("====")
            params = line.split('\t')
            print(params[0])
            result = template % (params[0], params[1], params[2], params[3].strip('\n'))
            # print(result)
            write.write(result)
            write.write('\n')
        print("over")

if __name__ == '__main__':
    initScrip()