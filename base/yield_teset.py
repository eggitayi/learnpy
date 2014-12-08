def func():
	for i in range(10):
		yield i
		yield 'd:'+str(i*2)

itr = func()
print '1:', itr.next()
print '2:', itr.next()
print '3:', itr.next()
print '4:', itr.next()
'''
print '5:', itr.next()
print '6:', itr.next()
'''