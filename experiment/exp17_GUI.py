import tkinter


root = tkinter.Tk()  # 根节点
lable = tkinter.Label(root, text="Hello python")  # 标签组件
lable.pack()
button1 = tkinter.Button(root, text="Button1")  # 按钮组件
button1.pack(side=tkinter.LEFT)
Quit = tkinter.Button(root,
                      text="quit",  # 文本内容
                      command=root.quit,  # 绑定退出动作
                      bg='red',  # 背景色
                      fg='blue',  # 前景色
                      width=8,  # 宽度
                      height=1,  #高度
                      justify=tkinter.RIGHT,
                      )
Quit.pack(side=tkinter.RIGHT)
root.mainloop()  # 刷新界面并while(1)
