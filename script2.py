import os
import time

def initScrip():
    readFilename = 'C:\\Users\\ediso\\Desktop\\coupon-raw.txt'
    writeFilename = 'C:\\Users\\ediso\\Desktop\\coupon-ripe.txt'

    # write = open(writeFilename, 'a')
    read = open(readFilename, 'r')

    lines = read.readlines() # 读取所有行
    template = "db.cdt_shop_point.update({shopId:%s},{$set:{isCoupon: NumberInt(1)}},{multi:true});"
    print(len(lines))
    with open(writeFilename, 'a') as write:
        for line in lines:
            print("====")
            params = line.split('\t')
            print(params[0])
            result = template % params[0].strip('\n')
            # print(result)
            write.write(result)
            write.write('\n')
        print("over")
    read.close()

if __name__ == '__main__':
    initScrip()