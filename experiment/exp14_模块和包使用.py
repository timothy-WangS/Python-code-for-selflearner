import exp14M_模块工具 as Exp14M  # 导入并指定其别名,大驼峰，必须"模块名."调用
from exp14P_模块工具 import Cat  # 导入指定工具(类，函数，全局变量)；若导入同名工具，使用后导入的
# from exp14P_模块工具 import *  # 不推荐，有同名覆盖无提示
# 导入时先查看当前目录，若没有则查看py系统目录；自定义模块不建议与系统模块同名

import exp14Pa_包  # 导入包中的所有文件，包需要有__init__.py文件控制调用许可
#发布模块：建立setup文件，其余步骤见experiment/setup.py文件
# 安装与卸载模块：见experiment/setup.py文件

Jone = Exp14M.Man("Jone")
Jone.work()

Exp14M.say()

Tom = Cat("Tom")
Tom.eat()

exp14Pa_包.exp14Pa_send.send("发送测试")
print(exp14Pa_包.exp14Pa_receive.receive())
