from tkinter import *

def reg():
    s1 = e.get()
    s2 = e2.get()
    len_s1 = len(s1)
    len_s2 = len(s2)
    if s1=='wd' and s2=='1998315':
        l3['text'] = '登录成功'
    else:
        l3['text'] = '用户名或密码错误'
        e.delete(0, len_s1)
        e2.delete(0, len_s2)


root = Tk()

l = Label(root, text='账号：')
l.grid(row=0, column=0, sticky=W)
e = Entry(root)
e.grid(row=0, column=1, sticky=E)

l2 = Label(root, text='密码：')
l2.grid(row=1, column=0, sticky=W)
e2 = Entry(root, show='*')
e2.grid(row=1, column=1, sticky=E)

b = Button(root, text='登录', command=reg)
b.grid(row=2, column=1, sticky=E)

l3 = Label(root, text='')
l3.grid(row=3, column=0, sticky=W)

root.mainloop()
