a = 1
b = 2
c = 3
d = 'a'
e = 'b'
f = 'c'

# if 缩进建议4个空格
if a == 1:
    print('a == 1')
else:
    print('no')

# 逻辑运算 and or not
if a == 1 and b == 1 or c == 3:
    print('ya')
else:
    print('oops')

# elif 就是else if
if a == 2:
    print(1)
elif a == 1:
    print(2)
else:
    print(0)

# if 的嵌套
if a == 1:
    if b == 3:
        print('ok')
    else:
        print('oh?')
else:
    print('no')

# while 语句
a = 0
while a <= 6:
    a += 1
    print('a = %d' % a)

# for循环(只用于迭代)
a = 'abc'
for tmp in a:
    print(tmp+" ", end="")
print("")
# 使用for的运算
numList = [1, 2, 3, 4]
squNumList = [x ** 2 for x in numList]
for tmp in squNumList:
    print(str(tmp)+" ", end="")
else:
    print("aaa")  # 迭代完成后执行，除非for被break结束
print("")

# break 和 continue
a = 0
while a <= 6:
    a += 1
    if a == 3:
        break  # 结束循环
    print('a = %d' % a)

a = 0
while a <= 6:
    a += 1
    if a == 3:
        continue  # 跳过当次后续
    print('a = %d' % a)

# pass 占位符,保障代码结构，不作任何操作
if a == 0:
    pass
else:
    a = 1
