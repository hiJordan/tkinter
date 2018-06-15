from tkinter import *

root = Tk()

root.title('原窗体')
l = Label(root, text='属于原窗体')
l.pack()

top = Toplevel(root, width=30, height=20)
top.title('新窗体')
l = Label(top, text='属于新窗体')
l.pack()
top.destroy()

root.mainloop()
