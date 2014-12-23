# coding: UTF-8
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

    one = getattr(module, 'one')
    one.introduce()
    print one.name
    one.name = "TWO"

    __module = __import__(module_name)
    print "#__MODULE - ", __module
    __one = getattr(module, 'one')
    __one.introduce()


if __name__ == '__main__':
    main()  # 啊啊哈
