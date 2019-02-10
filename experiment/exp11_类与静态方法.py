class Tool(object):
    count = 0  # 类属性

    @classmethod  # 定义类方法；只访问类属性
    def show_count(cls):  # 类方法(cls)
        print(cls.count)  # 在类中用cls.调用类属性或其他类方法

    @staticmethod  # 不使用类属性或实例化后的对象属性，则用静态
    def my_add(a, b):  # 不指定第一个参数self或cls
        c = a+b
        return c

    def __init__(self, name):
        self.name = name
        print("新建实例 %s" % self.name)
        Tool.count += 1  # 在类中用cls.调用类属性或其他类方法


tool1 = Tool("a")
tool2 = Tool("b")
tool2.count = 4  # 新增对象属性，不改变类属性
print(tool1.count)  # 用实例化的对象名(不推荐)或类名(若变量无此属性)访问类属性
Tool.show_count()  # 直接使用类方法，不实例化


p = 2
q = 3
tmp = Tool.my_add(p, q)  # 直接使用类的静态方法，不实例化
print(tmp)
