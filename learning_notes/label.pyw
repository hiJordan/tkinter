
from tkinter import *

root = Tk()
root.wm_title('tkinter')
w1 = Label(root, text='tkinter学习', bg='green')
w2 = Label(root, text='python学习', bg='red')
w1.pack()
w2.pack()

root.mainloop()
