class Person(object):
    def __init__(self, name, age=10):
        self.name = name
        self.age = age

    def say(self, content="nothting"):
        print "%s : %s" % (self.name, content)

    def leave(self):
        print "%s left" % (self.name)

    def introduce(self):
        print "My name is %s, and I'm %s now" % (self.name, self.age)

if __name__ == '__main__': 

    lily = Person('Lily', 14)
    lily.introduce()
    lily.say("WTF")
    lily.leave()