# -*- coding:utf-8 -*-

import keyword
# print("hello")  行注释'#',在其后要加空格
print("hello")  # 把注释直接加在代码后，需要2个空格

"""
多行注释
三对连续引号
单引号双引号都可以
"""
# 定义变量直接定义int(python2 中有 long),float(double),str,bool,complex(复数)，None(无)
a = 10
b = 2 ** 32 + 1
c = 1.3
d = 'a'
e = "del"
f = False  # false为0，true为1
n = None
print(a, b, c, d, e, f)

# 其他类型：列表，元组，字典
lisT = [1, 2, 3, 4, 5]
tuplE = ("a", "b", 1, 2)
dicT = {
    "name": "Jack",
    "NUM": "13"
}

# 标识符有字母数字下划线，不以数字开头，不能使用关键字，变量方法下划线，类驼峰，大小写敏感
print(keyword.kwlist)

# 变量类型改变
print(type(a))
a = '5'
print(a)
print(type(a))
tmp = int(a)
print(type(tmp))

# 加(连接)+  减-  乘(重复)*  除/   取整除//  余%  幂**，优先级(),**,*/%//,+-,同级左至右
# 赋值运算 += -= *= /= //= %= **=
print(1+2, 3-4, 2*3, 9/2, 9//2, 7 % 2, 2**3, 'c'*3, 'a'+'b')  # 'c'*3表示c重复3次,'a'+'b'代表连接,字符串与数字不可直接运算

# 类型转换
p = "1"
q = int(p)
print(q, type(q))
q = float(p)
print(q, type(q))
q = str(p)
print(q, type(q))
q = bool(p)
print(q, type(q))

# 转义字符
print("\\  \'  \"  \r  \n  \t")  # 反斜线，单引号，双引号，回车，换行，Tab

# 使用r使原字符保留，不考虑转义（常用于正则）
print(r"\r \n")

# 格式化输出 %d %s %f 整数，小数，字符串，百分号 %%
print("字符串p是 %s ，百分号是 %%" % p)
print("数字c是 %.4f，b是 %012d" % (c, b))

# 获取输入,结果都是字符串
tmp = input("请输入")
print(tmp)

# 在print后不增加换行
print("hello", end="")
print("world")

# TODO(负责该部分编程的人) 待做任务名称
# shift + F6 修改所有同名变量
