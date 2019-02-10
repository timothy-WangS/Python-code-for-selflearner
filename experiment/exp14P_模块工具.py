class Cat(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s is eating" % self.name)


class Dog(object):
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("%s is barking" % self.name)
