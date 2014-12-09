'''
decorator with parameter test
'''

def salesgirl(discount):
    def serve(method):
        def wrapper(*args, **kwargs):
            print 'Salesgirl: Hello, what do you want? ', method.__name__
            result = method(*args, **kwargs)
            if result:
                print 'Salesgirl: This one is 40$, we promised discount at %d%%' % discount
            else:
                print 'Salesgirl: Well, how about another one?'
            return result
        return wrapper
    return serve


    
@salesgirl(50)
def try_this_one(size):
    if size < 35:
        print "I: %d inches is to small to me" %(size)
        return False
    else:
        print "I:%d inches is just enough" %(size)
        return True
result = try_this_one(38) 
print result
