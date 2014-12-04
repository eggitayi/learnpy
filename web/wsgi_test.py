from wsgiref.simple_server import make_server

def myWebapp(environ, start_response):
	start_response('200 OOOK', [('Content-Type', 'text/html')])
	return '<h1>Hello, %s</h1>' % (environ['PATH_INFO'][1:] or 'web')


httpd = make_server('', 8000, myWebapp)
print "Serving HTTP on port 8000..."
httpd.serve_forever()