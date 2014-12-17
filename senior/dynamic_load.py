def main():
	module_name = "my_module"
	class_name = "Person"

	module = __import__(module_name)
	print "# MODULE - ", module
	cls = getattr(module, class_name)
	print "# CLASS - ", cls
	lucy = cls("Lucy")
	print "# OBJECT - ", lucy
	lucy.introduce()
	lucy.leave()

if __name__ == '__main__':
	main()