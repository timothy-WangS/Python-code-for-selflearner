class Animal(object):  # 以object为父类，新式类，建议加上；在py3中不指定，默认obj父类
    """全体动物"""
    def __init__(self, name):
        self.name = name
        self.__gene = "DNA"  # 私有

    def eat(self):
        print("%s eat" % self.name)

    def run(self):
        print("%s run" % self.name)

    def sleep(self):
        print("%s sleep" % self.name)

    def change_gene(self, gene):
        self.__gene = gene
        print("Error %s" % self.__gene)


class Cat(Animal):  # class 子类(父类)
    """全体猫"""
    def catch(self):
        print("%s catch" % self.name)

    def eat(self):
        print("%s eat mouse" % self.name)  # 覆盖重写

    def show_gene(self):
        print(self._Animal__gene)  # 子类不能调用父类的私有变量，方法


class FourLeg():  # 在py3以obj为父类，在py2无父类；建议加上object
    def __init__(self, name):
        self.name = name

    def fall(self):
        print("four legs %s fall" % self.name)


class Dog(Animal, FourLeg):  # 多继承,有相同方法，变量时慎用
    """全体狗"""
    def bark(self):
        print("%s bark" % self.name)


class CopyCat(Cat):  # 继承传递
    """猫中的模仿者"""
    def copy(self):
        print("CopyCat %s" % self.name)

    def run(self):
        super().run()  # 调用父类，如果父类没重写则看父父类
        print("FIND THAT CopyCat")


Tom = Cat("Tom")
Tom.eat()
Tom.catch()
Tom.run()
Tom.show_gene()
Tom.change_gene("RNA")  # 间接访问私有
# Tom.bark()  # 不可调用 Dog 类

Marry = CopyCat("Marry")
Marry.eat()  # 使用重写的方法
Marry.sleep()
Marry.run()

AHuang = Dog("AHuang")
AHuang.fall()
AHuang.bark()
