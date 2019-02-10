import threading
from time import sleep, ctime


loops = [4, 2]


def loop(nloop, nsec):
    print("start loop", nloop, "at", ctime())
    sleep(nsec)
    print("done loop", nloop, "at", ctime())


if __name__ == '__main__':
    print("start at", ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))  # 提供一个线程对象函数，参数
        threads.append(t)

    for i in nloops:
        threads[i].start()  # 开始线程

    for i in nloops:
        threads[i].join()  # 线程挂起直到结束

    print("done at", ctime())
