# 文件名就是模块名，用数字，字母，下划线，不可以数字开头
# 使用import，会生成该模块在pycache目录下编译过的.pyc二进制文件，提高速度


def my_add(a, b):  # 用于exp03
    return a + b  # 返回值


def my_multi(a, b):  # 用于exp03
    return a*b


def measure():
    return "len", "wid"  # 利用元组返回多个值，不加小括号----return ("len", "wid")
