from tkinter import *

#button's command parameter and .bind() function 

def add_label():
    global root
    display = Label(root, text='Python', bg='purple',
                    fg='white')
    display.pack()

root = Tk()
add = Button(root, text='Add a label', command=add_label,
             bg='pink', width=10, height=2)
add.pack()
root.mainloop()

'''
def add_label(event):
    global root
    dispaly = Label(root, text='Python')
    dispaly.pack()
root = Tk()
add = Button(root, text='Add a label')
add.bind('<Button-1>', add_label)
add.pack()
root.mainloop()
'''
