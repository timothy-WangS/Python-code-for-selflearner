# 分享开发的模块
from distutils.core import setup  # 不可变更
setup(
    name="exp14Pa_包",  # 包名
    version="版本号",
    description="描述信息",
    long_description="长描述",
    author="作者名",
    author_email="作者邮件",
    url="作者主页",
    py_modules=["exp14Pa_包.exp14Pa_send",
                "exp14Pa_包.exp14Pa_receive"]  # 要发布的模块
)
# 在终端进入experiment目录,输入"python3 setup.py build",如果是py2文件，改成python2
# 在experiment生成build目录
# 在终端experiment目录,输入"python3 setup.py sdist"
# 生成dist目录，可以发布.tar.gz文件

#安装模块：
# 终端输入 "tar -zxvf ***.tar.gz" ***为文件名
# 终端输入"sudo python3 setup.py install" 注意py3与py2
#
#卸载模块：
# 终端用"cd /user/local/lib/python3.5/disp-packages/"进入py目录
# "sudo rm -r 文件名*"  注意文件名后加*
#
#用pip安装卸载
#安装：sudo pip3 install 模块名
#卸载：sudo pip3 uninstall 模块名
#在py2中 pip3->pip
