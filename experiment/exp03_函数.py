import exp04_函数模块  # 每行只导入一个模块，遵循标准库模块，第三方模块，自定义模块的顺序


def my_add(a, b):  # 函数名小写、函数参数表定义方式
    """加法与连接"""  # 用于快速文档，Ctrl+q
    return a+b


def change_position1(a, b, *extraargs):  # extraargs是元组，用于容纳多余的传参，必须放在最后
    """交换
    
    :param a: 变量1
    :param b: 变量2
    """   # 添加变量的文档注释,Ctrl+q
    c = b  # 这是形参
    b = a
    a = c  # 赋值不影响实参的不可变参数与可变参数，修改(包括+=即extend)可影响可变参数
    print(a, b)
    for extra in extraargs:
        print(extra)


# 函数之后需要两行空行
print(my_add(2, 5))

a = 1
b = 2
print("%d %d" % (a, b))
change_position1(a, b)
# a, b = b, a  # python专属，利用元组，省略小括号，即a, b = (b, a)
print("%d %d" % (a, b))  # 无法交换实参

# 来自exp04
print(exp04_函数模块.my_add(5, 6))
print(exp04_函数模块.my_multi(2, 3))
print(exp04_函数模块.measure()[0], exp04_函数模块.measure()[1])  # 利用角标接受多返回
tmp1, tmp2 = exp04_函数模块.measure()  # 利用多变量接受返回，变量数应一致
print(tmp1, tmp2)

# 匿名函数lambda
a = lambda x, y: x+y
print(a(3, 4))
a = lambda x, y=2: x+y
print(a(3))
