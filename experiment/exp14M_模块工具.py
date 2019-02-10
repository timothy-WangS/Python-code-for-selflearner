title = "模块exp14M"


def say():
    print("hello")


class Man(object):
    def __init__(self, name):
        self.name = name

    def work(self):
        print("%s is working" % self.name)


print("开发模块exp14M测试")  # 导入模块时没有缩进的代码都会被执行一遍，这些代码不是提供的工具
if __name__ is "__main__":  # __name__若是主执行，则为"__main__";被调则为模块名
    print("带__name__的测试")

# 优秀的模块格式
"""
def main():
    模块测试代码

if __name__ is "__main__":
    main()
"""
