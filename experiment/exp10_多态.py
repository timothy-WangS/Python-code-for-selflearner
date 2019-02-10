class Animal(object):
    """全体动物"""
    def __init__(self, name):
        self.name = name
        self.__gene = "DNA"  # 私有

    def play(self):
        print("%s play" % self.name)


class Cat(Animal):
    def play(self):
        print("%s play mouse" % self.name)


class Dog(Animal):
    def play(self):
        print("%s play tick" % self.name)


class Man(object):
    def __init__(self, name):
        self.name = name

    def play(self, animal):
        print("%s play with %s" % (self.name, animal.name))
        animal.play()


Jone = Dog("Jone")
Tom = Cat("Tom")
Tim = Man("Tim")
Tim.play(Jone)
Tim.play(Tom)  # 不修改Man的代码即可完成，多态