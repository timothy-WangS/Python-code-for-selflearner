# 类创建的对象只有唯一实例
class LOnlyMe(object):  # 懒汉式
    __instance = None  # 记录第一个创建的对象
    __init_flag = False  # 用于只初始化一次

    def __new__(cls, *args, **kwargs):  # 分配空间，返回对象引用
        print("创建对象，分配空间")
        if cls.__instance is None:  # 如果未创建
            cls.__instance = super().__new__(cls)
            return cls.__instance  # 必须返回，才能得到创建的地址
        else:
            return cls.__instance  # 直接返回创建的对象

    def __init__(self):
        if self.__init_flag is True:  # 如果已经初始化过，则不再初始化
            return
        print("初始化")
        self.__init_flag = True


only1 = LOnlyMe()
print(only1)
only2 = LOnlyMe()
print(only2)
