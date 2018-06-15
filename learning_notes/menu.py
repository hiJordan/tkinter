
#主菜单与菜单项
from tkinter import *

'''
def tip():
    Label(root, text='Forever').pack()
'''
root = Tk()
menu_bar = Menu(root)

f_menu = Menu(menu_bar)
for item in ['新建', '打开', '保存', '另存为']:
    f_menu.add_command(label=item)
    #f_menu.add_separator() 添加分隔符

e_menu = Menu(menu_bar)
for item in ['剪贴', '复制', '粘贴']:
    e_menu.add_command(label=item)

v_menu = Menu(menu_bar)
for item in ['默认', '新式']:
    v_menu.add_command(label=item)

i_menu = Menu(menu_bar)
for item in ['版权信息', '其他说明']:
    i_menu.add_command(label=item, accelerator='ss')
    #i_menu.add_command(label=item, command=tip)

t_menu = Menu(menu_bar)
for item in [1, 2, 3, 4, 5]:
    t_menu.add_radiobutton(label=item)
    #t_menu.add_checkbutton(label=item) 多选按钮

all_menu = [f_menu, e_menu, v_menu, i_menu, t_menu]
menu_item = ['文件', '编辑', '视图', '关于', '测试']
for item, item_info in zip(menu_item, all_menu):
    menu_bar.add_cascade(label=item, menu=item_info)

root['menu'] = menu_bar
root.mainloop()

'''
from  tkinter import *

def tip():
    global root
    Label(root, text='Love Python').pack()

def pop(event):
    menu_bar.post(event.x_root, event.y_root)
 
root = Tk()
menu_bar = Menu(root)
items = ['C', 'Java', 'C++']

for item in items:
    menu_bar.add_command(label=item)
menu_bar.add_command(label='Python', command=tip)

root.bind('<Button-3>', pop)
#root['menu'] = menu_bar 加上后itmes中内容变为顶层菜单
root.mainloop()
'''
