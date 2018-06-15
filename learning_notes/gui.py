import tkinter

top = tkinter.Tk()

hello = tkinter.Label(top, text='hello')
hello.pack()

quits = tkinter.Button(top, text='quit',
        command=top.quit, bg='red', fg='white')
quits.pack(fill=tkinter.X, expand=1)

tkinter.mainloop()
