from tkinter import *

root = Tk()
Label(root, text='账户：').grid(row=0, sticky=W)
Entry(root).grid(row=0, column=1, sticky=E)

Label(root, text='密码：').grid(row=1, sticky=W)
Entry(root).grid(row=1, column=1, sticky=E)

Button(root, text='登录').grid(row=2, column=1, sticky=E)
root.mainloop()
