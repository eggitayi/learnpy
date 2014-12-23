import time
import threading

ll = []
for x in range(10000):
    ll.append(x)


def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>>> %s' % (threading.current_thread().name, n)
        time.sleep(0.2)
    print 'thread %s is dead' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread %s end...' % threading.current_thread().name


def passmethod():
    pass

passmethod()
