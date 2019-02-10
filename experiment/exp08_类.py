# 使用驼峰法命名
class People:
    """这是一个人类"""  # 文本注释
    def __init__(self):  # 内置函数，以"__"开头和结尾
        print("初始化")

    def eat(self, sth):  # 第一个参数必须是self，其他与定义函数一致
        print("%s eat %s" % (self, sth))

    def drink(self, sth):  # 两个方法之间空一行
        print("%s drink %s" % (self, sth))

    def say_age(self):
        print(self.age)  # 用self输出属性


class Cat:
    """这是一个猫类"""
    def __init__(self, name="cat"):  # 参数初始化，不必须使用默认参数
        self.name = name  # 在初始化中定义属性并赋初值

    def say_name(self):
        print(self.name)

    def __del__(self):  # 从内存中销毁之前调用
        print("%s 被销毁" % self.name)

    def __str__(self):  # 对象输出，必须返回字符串
        return "This is %s" % self.name


class Worker:
    def __init__(self, salary):
        self.__salary = salary  # 私有属性(伪)

    def __secrete(self):  # 私有方法(伪)
        print("%s do secrete things" % self)

    def say_salary(self):
        print(self.__salary)

    def be_found(self):
        self.__secrete()


Jack = People()  # 创建对象(实例)->分配空间->初始化__init__->；类定义完空两行
Jack.eat("fish")  # 使用类方法
Jack.drink("tea")

Oliver = People()  # 不同对象
Oliver.eat("meat")

Alice = Jack  # 同一对象
Alice.eat("cake")
Alice.age = 18  # 增加实例属性，不改变类属性或其他同类属性
print(Jack.age)
Jack.say_age()

Tom = Cat()  # 默认初始化
Tom.say_name()
Tom.name = "Tom"
Tom.say_name()

Jerry = Cat("Jerry")  # 初始化其参数
Jerry.say_name()
print(Jerry)  # 输出__str__返回值
del Jerry  # 手动销毁，其他对象在关闭时自动销毁

Jim = Worker(3000)
# print(Jim.__salary)  # 无法使用，外部不可直接调用
# Jim.__secrete()  # 无法使用，外部不可直接调用
Jim.say_salary()  # 通过对象访问
Jim.be_found()
Jim._Worker__secrete()  # python实际上是改变了变量名=>_类名__变量、方法名(不建议这样调用)
