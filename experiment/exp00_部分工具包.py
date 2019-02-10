# 随机数
import random
a = random.randint(10, 20)  # 输出括号内的随机范围int数，含头尾
print(a)
# a = random.randint(20,10) 错误，下限要小于上限
a = random.randint(20, 20)
print(a)  # 永远是20

# range()函数,从0到指定值的列表
for tmp in range(6):
    print(str(tmp)+" ", end="")
print("")

# open(),file()函数，打开文件
fileName = "F:\program\Python\experiment\TestFiles\exp00.txt"
fileContentTmp = open(fileName, 'r')
for tmp in fileContentTmp:
    print(tmp, end="")
print("")
fileContentTmp.close()

b = [2, 3, 4, 5, 4, 3, 3]
# del + 变量名或列表[角标] 从内存删除变量，后续代码不能再使用
del a
del b[0]
del(b[0])

# len + 变量名 返回变量长度
print(len(fileName))

# max + 变量名 返回最大值(min返回最小值),字典为key值
tmp = max(b)

# cmp就是>,<,=,也可用于列表，元组，不可用于字典，"0"<"A"<"a"
print("a" < "b")

# [::] 切片用于字符串，列表，元组(exp05), [start:end:step](start,end为负则指反向)  [start:end]；不可用于字典
tmpp = b[1:5]  # 从角标为2到5 (0,1,2,3,4,5...),(可选)默认步长为1
print(tmpp)
tmpp = b[::-1]  # 反转
print(tmpp)

# in,not in 包含，不包含，在字典中判断键而不是值
print(4 in b)
print("4" not in b)

# is, is not 判断id相同，不同；==判断值
c = 12
d = "12"
print(c is d)
print(c == d)

# hash 不可变元素（数字，字符串等）元素特征码（除了列表，字典）
print(hash("a"))

# dir函数 用于检测方法可使用的内置函数
print(dir(b))


# apply(已废弃),filter,map
def odd(n):
    return n % 2  # 偶数返回0(False)


allnums = []
for each in range(9):
    allnums.append(random.randint(1, 99))  # 生成随机1~99
print(filter(odd, allnums))  # 保留奇数, 此处odd可用lambda代替，打印的是filter引用


"""def map(func, seq):  # map内置函数的函数结构
    mapped_seq = []
    for eachItem in seq:
        mapped_seq.append(func(eachItem))
    return mapped_seq
"""

print(map((lambda x: x+2), [0, 1, 2, 3, 4, 5, 6, 7]))
