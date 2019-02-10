# 不可变类型：int float,complex,long,boolean,str,tuple(元组),
# 可变类型：list(列表),dict(字典)
# 全局与局部变量
gnum = 10  # 建议在函数定义前，import后(可以定义在模块任意位置，但必须在调用“使用了该变量的函数”前)
g_num = 10  # 规范的全局变量定义方式"g_"和"gl_"

def demo1():
    num = 1
    print("demo1 %s" % num)
    gnum = 6  # 创建一个同名局部变量
    print("demo1 %s" % gnum)  # 局部变量被修改


def demo2():
    # print(num)
    num = 2
    print("demo2 %s" % num)
    print("demo2 %s" % gnum)  # 全局变量的值未修改


def demo3():
    global gnum
    gnum = 6


def demo4():
    print(gnum)  # 全局变量被修改


# 缺省参数，设置最常见的值简化函数，如print的end=
def demo5(pri=True):  # pri缺省为True，缺省参数置于末尾
    if pri:
        print("aaa")


# 多值参数，*元组，**字典
def demo6(*args, **kwargs):  # 调用时也要加*，**拆包
    print(args)
    print(kwargs)


# 递归
def my_sum(n):
    if n == 1:
        return 1
    return n + my_sum(n-1)


demo1()
demo2()
demo3()
demo4()
print(my_sum(4))
