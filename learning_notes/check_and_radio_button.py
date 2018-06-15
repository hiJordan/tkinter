from tkinter import *

def test_cb_1():
    global time_1
    if time_1 % 2 == 0:
        time_1 += 1
        l_1['text'] = '2015已选中'
    else:
        time_1 += 1
        l_1['text'] = '2015未选中'

def test_cb_2():
    global time_2
    if time_2 % 2 == 0:
        time_2 += 1
        l_2['text'] = '2016已选中'
    else:
        time_2 += 1
        l_2['text'] = '2016未选中'

def test_rb():
    global time_3
    if time_3 % 2 == 0:
        time_3 += 1
        l_3['text'] = '2017已选中'
    else:
        time_3 += 1
        l_3['text'] = '2017未选中'

time_1 = 0
time_2 = 0
time_3 = 0
root = Tk()

cb_1 = Checkbutton(root, text='2015', command=test_cb_1)
cb_1.pack()
cb_2 = Checkbutton(root, text='2016', command=test_cb_2)
cb_2.pack()
rb = Radiobutton(root, text='2017', command=test_rb)
rb.pack()

l_1 = Label(root, text='')
l_1.pack()
l_2 = Label(root, text='')
l_2.pack()
l_3 = Label(root, text='')
l_3.pack()

root.mainloop()
