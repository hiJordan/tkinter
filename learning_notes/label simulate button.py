from tkinter import *

def display(event):
    global root
    simulate = Label(root, text='模拟成功')
    simulate.pack()

root = Tk()
simulate = Label(root, text='模拟按钮')
simulate.bind('<Button-1>', display)
simulate.pack()
root.mainloop()
