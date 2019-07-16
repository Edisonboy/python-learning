import sys
import time
import requests

# 接口批量调用

# 请求地址
url = 'xxx'             #测试
# 读取文本地址
readFilename = 'add.txt'
# 写入文本地址
writeFileName = 'error.txt'
# 成功数目
successNum = 0;
# 失败数据
failNum = 0;

def run():
    global successNum
    with open(readFilename) as file_object:
        contents = file_object.read()
        array = contents.split(',')
        print('add data nums: %s' % len(array))
        for a in array:
            requestUrl = url % a.strip()
            print(requestUrl)
            response = requests.get(requestUrl)
            print('result: %s ' %response.json())
            # 判断结果是否正确
            flag = response.status_code != 200 or response is None
            if flag:
                fail(a)
                continue
            json = response.json()
            print(json)
            if json.get('result') != 1:
                fail(a, json.get('message'))
                continue
            else:
                successNum += 1
                print('shopId: %s success' % a.strip()) 
            time.sleep(0.5)

# 记录请求失败
def fail(shopId, msg=''):
    global failNum
    failNum += 1
    print('fail, shopId: %s' % shopId)
    with open(writeFileName, 'a') as file_object:
        file_object.write(shopId)
        if msg.strip() != '':
            file_object.write(', %s' % msg)
        file_object.write('\n')

if __name__ == "__main__":
    # global url
    if len(sys.argv) != 2:
        print('error, param nums must 2')
        exit()
    arg = sys.argv[1]
    if arg == 'prod':
        url = 'xxx'
    elif arg == 'pre':
        url = 'xxx'
    elif arg == 'dev':
        url = 'xxx'
    else:
        print('param error')
        exit()
    run()
    print('data sync done....')
    print('successNum: %s - failNum: %s' % (successNum, failNum) )
