from tkinter import *

root = Tk()
Button(root, text='A').pack(side=LEFT, expand=1, fill=Y)
Button(root, text='B').pack(side=TOP, expand=YES, fill=BOTH)
Button(root, text='C').pack(side=RIGHT, expand=1, fill=NONE
                            , anchor=NE)
Button(root, text='D').pack(side=LEFT, expand=0, fill=Y)
Button(root, text='E').pack(side=TOP, expand=0, fill=BOTH)
Button(root, text='F').pack(side=BOTTOM, expand=1)
Button(root, text='G').pack(anchor=SE)
