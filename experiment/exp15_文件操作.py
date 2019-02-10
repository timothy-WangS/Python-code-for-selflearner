# 步骤 读文件，写文件，关文件
fileName = "F:\program\Python\experiment\TestFiles\exp15.txt"  # 存储文件名
aimFile = "F:\program\Python\experiment\TestFiles\exp15A.txt"  # 复制到目标文件

# open()函数，打开文件并返回文件对象
fileContentTmp = open(fileName, 'r+')
fileContentTmpA = open(aimFile, 'w')
"""r(默认)只读；w只写，覆盖或新建；a追加，追加或新建；----------更常用
r+读写，指针放开头；w+读写，覆盖或新建；a+追加，追加或新建"""


# read()函数，读到内存
text = fileContentTmp.read()  # read结束后文件指针到末尾，再读无法得数据
print(text)
fileContentTmpA.write(text)

# readline()函数，一次读一行，循环，大文件使用
"""while True:
    text = fileContentTmp.readline()
    if not text:  # 不是文件(/r,/n,空格还是文件内容，不跳出)
        break
    print(text)
    fileContentTmpA.write(text)"""

# write()函数，写入文件，需要w或a方式
"""fileContentTmp.write("HaHaHa")"""

# 用close()，关闭文件
fileContentTmp.close()

# 常用管理操作，要导入os模块
"""
rename:重命名 os.(源文件名,目标文件名)
remove:删除 os.remove(文件名)
listdir:目录列表 os.listdir(目录名)
mkdir:创建目录 os.mkdir(目录名)
rmdir:删除目录 os.rmdir(目录名)
getcwd:当前目录 os.getcwd()
chdir:变更工作目录 os.chdir(目标目录)
path.isdir:判断是否是文件 os.path.isdir(文件路径)
"""

# 文件编码 py2 ASCII；py3 utf-8
# py2 改变编码：在文件第一行写上# *-* coding:utf8 *-* 或 # coding = utf8
# py2 遍历字符串时还要写 u"字符串" 表明这是utf8