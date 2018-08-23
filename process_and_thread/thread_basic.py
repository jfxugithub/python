'''
Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。
                          绝大多数情况下，我们只需要使用threading这个高级模块。
注意：进程是至少有一个线程组成
启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
'''
import time,threading

def loop (s):
    tStart = time.time()
    time.sleep(s)
    tEnd = time.time()
    print("%s run %s seconds and it is over" % (threading.current_thread().name,tEnd - tStart))


def threading_basic():
    print("%s is runninng..." % threading.current_thread().name)
    t = threading.Thread(target=loop, args=(1,), name="LoopThread")  # 返回当前线程的实例
    t.start()  # 启动子线程
    t.join()  # 加入主线程，使主线程等子线程结束后再继续往下走


# threading_basic()
"""====================================================================================="""

"""
线程锁 threading.Lock()
"""

total_varial = 0

def change_it(n):
    global total_varial
    total_varial += n
    total_varial -= n

def run_thread(n):
    for i in range(1000000):
        change_it(n)

def unlock_thread_test():
    t1 = threading.Thread(target=run_thread, name="Thread_1", args=(1000,))
    t2 = threading.Thread(target=run_thread, name="Thread_2", args=(5000,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("因为没有加锁，所以全局变量的值 不一定是0，total_varial = %d" % total_varial)

# unlock_thread_test()

lock = threading.Lock()     #创建锁

def run_thread_locked(n):
    lock.acquire()          #获取锁
    for i in range(1000000):
        change_it(n)
    lock.release()          #释放锁


def locked_thread_test():
    t1 = threading.Thread(target=run_thread_locked, name="Thread_1", args=(1000,))
    t2 = threading.Thread(target=run_thread_locked, name="Thread_2", args=(5000,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("线程加锁后全局变量的值将会保持不变，total_varial = %d" % total_varial)

# locked_thread_test()
'''
ThreadLocal变量:虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
'''

localVal = threading.local()  #创建一个ThreadLocal对象的实例
def thread_run(name):
    localVal.name = name    #动态添加属性name
    show_stu()

def show_stu():
    name = localVal.name   #获取当前线程中localValue的name属性值
    print("student name is %s (%s):" % (name,threading.current_thread().name))


def thread_local_test():
    t1 = threading.Thread(target=thread_run, args=("julia",), name="Thread_A")
    t2 = threading.Thread(target=thread_run, args=("alen",), name="Thread_B")
    t1.start()
    t2.start()
    t1.join()
    t2.join()


# thread_local_test()




















