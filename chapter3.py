import asyncio
import threading

# 协程
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print("[CONSUMER] consuming %s ..." % n)
        r = '200 OK'


def produce(c):
    # 启动生成器
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print("[PRODUCER] producing %s ..." % n)
        r = c.send(n)
        print("[PRODUCER] consumer return: %s " % r)
    c.close()


c = consumer()
produce(c)


# asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())


# 获取Eventloop
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()



