class myDecorator(object):
 
    def __init__(self, f):
        print "inside myDecorator.__init__()"
        #f() # Prove that function definition has completed
        self.f = f
 
    def __call__(self):
        print "inside myDecorator.__call__()"
        self.f()
 
@myDecorator
def aFunction():
    print "inside aFunction()"

#print "Finished decorating aFunction()"

aFunction()


def dec(method):
	def wrapper(*args):
		print 'in: ', args
		return method(*args)
	return wrapper
@dec
def method1(a, b):
	return a + b

@dec
def method2(a):
	return a * a

@dec
def method3(a, b, c):
	return a + b + c


print method1(1, 2)
print method2(3)
print method3(4, 5, 6)