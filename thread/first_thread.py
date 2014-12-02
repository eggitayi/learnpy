import time
import threading

def loop():
	print 'thread %s is running...' % threading.current_thread().name
	n = 0
	while n < 10:
		n = n + 1
		print 'thread %s >>>> %s' % (threading.current_thread().name, n)
		time.sleep(2)
	print 'thread %s is dead' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()


