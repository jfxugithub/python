'''
linux/unix 系统提供fork()系统调用
'''

import os
import time

def multiprocess_for_linux():

    pid = os.fork()  # 创建一个新进程，返回子进程的pid给父进程，返回0给子进程
    if pid == 0:
        mypid = os.getpid()  # 获取自身的pid
        myppid = os.getppid()  # 获取父进程的pid
        print("I am child process (%s) and my parent is %s." % (mypid, myppid))
    else:
        print("I (%s) just created a child process %s." % (os.getpid(), pid))


# multiprocess_for_linux()

'''
multiprocessing：跨平台通用多进程的实现
'''

from multiprocessing import Process


def Process_operation():
    global p

    def run_proc(name):
        print("Run child process %s (%s)..." % (name, os.getpid()))

    # if __name__ == "main" :
    print("Parent process %s..." % (os.getpid()))
    p = Process(target=run_proc, args=("test",))
    print("Child process will start...")
    p.start()
    p.join()
    print("Child process end.")


# Process_operation()

"""
使用线程池批量实现进程的创建
"""

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


def pool_operation():
    global p
    if __name__ == '__main__':
        print('Parent process %s.' % os.getpid())
        p = Pool(4)
        for i in range(5):
            p.apply_async(long_time_task, args=(i,))
        print('Waiting for all subprocesses done...')
        p.close()                                   #调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
        p.join()
        print('All subprocesses done.')


# pool_operation()