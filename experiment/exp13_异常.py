def div_num():
    num = False
    while num is False:
        try:
            num = int(input("请输入一个数字，做除法"))
            print(233/num)
        except ValueError:
            num = False
            print("值错误，必须输入数字")
        except ZeroDivisionError:
            num = False
            print("数错误，不能除以零")
        # except ****Error:  # 针对错误类型捕获异常，最后一行错误信息第一个单词
        except Exception as result:  # 未知异常的解决
            print("未知异常 %s" % result)  # result变量 接收解释器报出的异常名
        else:
            print("一切正常")  # try无异常，则执行
        finally:
            print("finally")  # 无论如何，在try-except-else-final语句块结束前，无论如何都执行

    print("-" * 50)


# 异常传递
def demo1():
    print(233/int(input("输入整数")))  # 有异常，抛给主调函数
    print("demo1结束")  # 有异常，返回demo1，不继续执行
    return


def demo2():
    try:  # 无处理，继续抛给主调函数（主函数）
        demo1()
    except ValueError:
        print("值错误，必须是数字")

    print("demo2结束")


# 主动抛出异常
def input_phone():
    ex = Exception("长度错误")
    num = input("请输入手机号")
    if len(num) != 11:
        raise ex
    else:
        print(num)

"""div_num()"""

"""try: # 主程序捕获异常
    demo2()
except Exception as result:
    print("未知异常 %s" % result)"""

try:
    input_phone()
except Exception as result:
    print(result)


