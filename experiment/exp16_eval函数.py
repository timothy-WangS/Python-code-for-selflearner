# 功能强大，成功返回0，失败报错
# eval把字符串转变为代码
tmp = eval("1+2*3")
print(tmp)

# 转换格式
tmp = eval("[1, 3, 6, 8]")
print(type(tmp))
tmp = eval("{1,3, 6, 9}")
print(type(tmp))

# 警告：不要滥用eval！
# 开发时不要直接用eval转换input的结果
