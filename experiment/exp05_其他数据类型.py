# 其他类型：列表，元组，字典，字符串
# 列表 **************************************************************
numList = [1, 2, 3, 4, 5, 2, 3, 4, 2, 3, 2]  # 建议只用一个类型元素，（支持多类型）
strList = ["abc", "def", "ghi"]
apdList = ["xyz", "pqr"]
# 取值
print(numList[0], strList[2])
# 取索引(第一个位置)
print(numList.index(2))  # 不存在会报错
# 遍历
for tmp in strList:
    print(tmp+" ", end="")
print("")
# 修改
numList[0] = 9  # 超过角标报错
# 增加
strList.append("zzz")  # 追加 值（或其他元素(如另一个列表等)，不推荐）
strList.insert(2, "aaa")  # 插入 角标+值
strList.extend(apdList)  # 附加 其他同类型列表
for tmp in strList:
    print(tmp+" ", end="")
print("")
# 删除
del strList[0]  # 删除指定数据
strList.remove("ghi")  # 删除第一个指定的数据
tmp = strList.pop(1)  # 删除并返回角标处数据
print("pop => "+tmp)
apdList.clear()  # 清空
for tmp in strList:
    print(tmp+" ", end="")
print("")
# 排序
numList.sort(reverse=False)  # 升序
print(numList)
numList.sort(reverse=True)  # 降序
print(numList)
# 其他
print(numList.count(2))  # 元素出现的次数
print(len(numList))  # 长度(最大角标+1)
# 元组 **************************************************************
infoTuple = ("Jack", "male", 1.75, 98)  # 定义之后不能修改，支持多类型
singTuple = ("undefined", )  # 单一元素要逗号结尾
empTuple = ()  # 定义空元组
# 取值
print(infoTuple[2])
# 取索引(第一个位置)
print(infoTuple.index("male"))  # 不存在会报错
# 遍历
for tmp in infoTuple:
    print(str(tmp)+" ", end="")
print("")
# 其他
print(infoTuple.count(1.75))  # 元素出现的次数
print(len(infoTuple))  # 长度(最大角标+1)
print("姓名 %s 性别 %s 身高 %.2f 成绩 %d" % infoTuple)  # 用于格式输出
# 类型转换 list <-> tuple
tmpList = list(infoTuple)
tmpTuple = tuple(strList)
print(type(tmpList), type(tmpTuple))
# 字典 **************************************************************
dataDict = {
    "name": "Oliver",
    "num": 29,
    "age": 18,
    "height": 1.75,
}
apdDict = {
    "weight": 60,
    "age": 20.
}  # "键": 无序的，键只能是字符串，数字，元组等不可变类型，不可为列表，字典等可变类型；值任意
# 取键列表
print(dataDict.keys())
# 取值列表
print(dataDict.values())
# 取键值对列表
print(dataDict.items())
# 取值
print(dataDict["name"])
# 遍历
for tmp in dataDict:
    print("%s %s" % (tmp, str(dataDict[tmp])))
# 增加
dataDict["score"] = 98  # 增加键值对
dataDict.update(apdDict)  # 合并字典(相同键的值覆盖)
# 修改
dataDict["num"] = 33
# 删除
dataDict.pop("height")
print(dataDict.items())
# 其他
print(len(dataDict))  # 统计键值对数
dataDict.clear()  # 清空
print(dataDict.items())
# 经常用列表存储字典
# 字符串 **************************************************************
strString = "   ABcdd efgg123ttt"
# 取字符
print(strString[3])
# 遍历
for tmp in strString:
    print(tmp+" ", end="")
print("")
# 其他(众多方法)
print(len(strString))  # 统计长度
print(strString.count("d"))  # 统计出现数
print(strString.index("c"))  # 出现位置角标
# 判断类型方法：is开头
tmp = strString.isupper()  # 全大写
print(tmp)
tmp = strString.islower()  # 全小写
print(tmp)
tmp = strString.isspace()  # 全空格
print(tmp)
tmp = strString.isnumeric()  # 全数字
print(tmp)
# 查找和替换
tmp = strString.startswith("aaa")  # 是否以"aaa"开头，返回Boolean
print(tmp)
tmp = strString.endswith("aaa")  # 是否以"aaa"结尾，返回Boolean
print(tmp)
tmp = strString.find("aaa")  # 从0位置查找是否包含"aaa"，返回"aaa"的位置或-1
print(tmp)
tmp = strString.rfind("aaa")  # 从末位置查找是否包含"aaa"，返回"aaa"的位置或-1(find)
print(tmp)
# tmp = strString.index("aaa")  # 从0位置查找是否包含"aaa"，返回"aaa"的位置或报错(find)
# print(tmp)
# tmp = strString.rindex("aaa")  # 从末位置查找是否包含"aaa"，返回"aaa"的位置或报错(find)
# print(tmp)
tmp = strString.replace("gg", "abc")  # 替换，不改变原有，返回新字符串
print(tmp)
# 大小写转换
tmp = strString.lower()  # 转小写，不改变原有，返回新字符串
print(tmp)
tmp = strString.upper()  # 转大写，不改变原有，返回新字符串
print(tmp)
tmp = strString.swapcase()  # 转换，不改变原有，返回新字符串
print(tmp)
tmp = strString.capitalize()  # 串首字母大写，不改变原有，返回新字符串
print(tmp)
tmp = strString.title()  # 每个单词首字母大写，不改变原有，返回新字符串
print(tmp)
# 文本对齐
tmp = strString.rjust(20)  # 右对齐，默认加空格补至指定长度，不改变原有，返回新字符串
print(tmp)
tmp = strString.ljust(20)  # 左对齐，默认
print(tmp)
tmp = strString.center(20, "_")  # 居中对齐，指定加"_"补至指定长度，不改变原有，返回新字符串
print(tmp)
# 去空格
tmp = strString.lstrip()  # 去左字符串(默认空白字符，换行和空格等)，不改变原有，返回新字符串
print(tmp)
tmp = strString.rstrip("t")  # 去右字符串(指定"t")，不改变原有，返回新字符串
print(tmp)
tmp = strString.strip(" ")  # 去两侧字符串(指定空格)，不改变原有，返回新字符串
print(tmp)
# 拆分和连接
tmp = strString.partition("ef")  # 左起查找"ef",拆分成ef，f前，
print(tmp)
tmp = strString.rpartition("ef")  # 右起查找"ef",拆分成ef，f前，
print(tmp)
tmp = strString.splitlines()  # 按行'/r''/n''/r/n'划分
print(tmp)
tmp = strString.split(" ", 4)  # 以" "拆分字符串，，默认包含最多拆分4次，舍去各" ",可能留下空的小字符串
print(tmp)
tmpp = " ".join(tmp)  # 把字符串数组拼合成tmpp字符串，用" "连接
print(tmpp)
tmp = strString[0:16:2]  # 切片保留小串的首字，从0到16，步长为2；各部分都可以省略，默认[0:末尾:1]；把16换成负数，则从末尾计数
print(tmp)
tmp = strString[-1::-1]  # 逆序，也可以[::-1]，[start:end:step]  [start:step]
print(tmp)
# 多修饰字符串
tmp = strString.strip().center(20)
print(tmp)
