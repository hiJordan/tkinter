from tkinter import *
from tkinter.dialog import *
from tkinter.messagebox import *
from tkinter.ttk import *


def pop_dialog():
    d = Dialog(None, title='调查', text='是否满意?',
               bitmap=DIALOG_ICON, default=0,
               strings=('是', '否'))


root = Tk()
b1 = Button(root, text='调查', command=pop_dialog)
b1.pack()
b2 = Button(root, text='关闭', command=root.quit)
b2.pack()
root.mainloop()
'''
showinfo(title='测试', message='test')
'''
