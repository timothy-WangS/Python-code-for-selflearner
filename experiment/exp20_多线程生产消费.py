import threading
from random import randint
from time import sleep
import queue


def writeQ(queue):
    print("produce Q....")
    queue.put("xxx", 1)
    print("size now", queue.qsize())


def readQ(queue):
    val = queue.get(1)
    print("consume Q....", queue.qsize())


def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        # sleep(randint(1, 2))
        sleep(0.14)


def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        # sleep(randint(1, 2))
        sleep(0.2)


funcs = [writer, reader]
nfuncs = range(len(funcs))


if __name__ == '__main__':
    nloops = randint(20, 30)
    q = queue.Queue()
    threads = []
    for i in nfuncs:
        t = threading.Thread(target=funcs[i], args=(q, nloops))  # 提供一个线程对象函数，参数
        threads.append(t)

    for i in nfuncs:
        threads[i].start()  # 开始线程

    for i in nfuncs:
        threads[i].join()  # 线程挂起直到结束

    print("done")
