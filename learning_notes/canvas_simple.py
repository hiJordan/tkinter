from tkinter import *
from tkinter.ttk import *

root = Tk()

root.title('简易绘图')
can = Canvas(root, width=400, height=300, bg='green')
can.create_line((0, 0), (200, 200), width=8)
can.create_text(300, 30, text='线段绘图')
can.pack()
root.mainloop()
