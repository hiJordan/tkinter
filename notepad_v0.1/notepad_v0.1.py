from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import os
import time

def f_new(event=None):
    global main_form, file_name, text_changed
    if text_changed:
        flag = askyesnocancel(title='记事本', message='是否将更改保存到 '+file_name+'?')
        if flag == True:
            f_save_as()
        elif flag == None:
            return
    file_name = '记事本 - 无标题'
    main_form.title(file_name)
    text_field.delete(1.0, END)
    text_changed = False

def f_open(event=None):
    global main_form, file_name
    if text_changed:
        flag = askyesnocancel(title='记事本', message='是否将更改保存到 '+file_name+'?')
        if flag == True:
            f_save()
        elif flag == None:
            return
    
    file_name = askopenfilename(filetypes=[('文本文档', '.txt')])
    if file_name == '':
        pass
    else:
        main_form.title('记事本 - '+os.path.basename(file_name))
        file = open(file_name, 'r')
        text_field.delete(1.0, END)
        text_field.insert(1.0, file.read())
        file.close()

def f_save(event=None):
    global file_name, main_form, text_field, text_changed
    if not text_changed:
        return
    if file_name == '记事本 - 无标题':
        f_save_as()
    else:
        file = open(file_name, 'w')
        text_field_content = text_field.get(1.0, END)
        file.write(text_field_content)
        file.close()
        text_changed = False

def f_save_as(event=None):
    global file_name, text_field, main_form, text_changed

    file_name = asksaveasfilename(initialfile=os.path.basename(file_name))
    if file_name == '':
        pass
    else:
        text_content = text_field.get(1.0, END)
        file = open(file_name, 'w')
        file.write(text_content)
        file.close()
        main_form.title('记事本 - '+os.path.basename(file_name))
        text_changed = False
    

def f_exit(event=None):
    global file_name, text_changed, main_form
    if text_changed:
        flag = askyesnocancel(title='记事本', message='是否将更改保存到'+file_name+'?')
        if flag:
            f_save()
        elif flag == None:
            return
    main_form.destroy()
    

def f_revoke(event=None):
    global text_field
    text_field.event_generate('<<Undo>>')

def f_cut(event=None):
    global text_field
    text_field.event_generate('<<Cut>>')

def f_copy(event=None):
    global text_field
    text_field.event_generate('<<Copy>>')

def f_paste(event=None):
    global text_field
    text_field.event_generate('<<Paste>>')

def f_del():
    pass

def f_find(event=None):
    global find_form, find_label, find_check, find_entry, find_all_button, find_cancel_button
    find_form = Toplevel(main_form)
    find_form.title('查找')
    find_form.geometry('280x80+200+250')
    find_form.transient(main_form)
    
    find_label = Label(find_form, text='查找:')
    find_label.grid(row=0,column=0, sticky='w')
    
    entry_content = StringVar()
    find_entry = Entry(find_form,width=20,textvariable=entry_content)
    find_entry.grid(row=0,column=1,padx=2,pady=2,sticky='we')
    find_entry.focus_set()
    
    check_content = IntVar()
    find_check=Checkbutton(find_form, text='区分大小写(C)', variable=check_content)
    find_check.grid(row=1,column=1,sticky='w')
    
    find_all_button = Button(find_form, text='查找全部(F)', command=lambda:f_search(entry_content.get(),check_content.get(), text_field,
                                                               find_form,  find_entry))
    find_all_button.grid(row=0, column=2, sticky='e'+'w',padx=2,pady=2)
    
    def close_find():
        text_field.tag_remove('match','1.0',END)
        find_form.destroy()
    find_cancel_button = Button(find_form, text='取消', command=close_find)
    find_cancel_button.grid(row=1, column=2, sticky='e'+'w',padx=2,pady=2)
    find_form.protocol('WM_DELETE_WINDOW',close_find)
    
        
def f_search(find_text,case,all_text,f_form,entry):
    all_text.tag_remove('match', '1.0', END)
    if find_text:
        pos = '1.0'
        while True:
            pos = all_text.search(find_text, pos, nocase=case, stopindex=END)
            if not pos:
                break
            lastpos = pos.split('.')[0]+'.'+str(int(pos.split('.')[1])+len(find_text))
            all_text.tag_add('match', pos, lastpos)
            pos = lastpos
        all_text.tag_config('match', foreground='white', background='blue')
        entry.focus_set()
        

def f_next(event=None):
    pass

def f_replace(event=None):
    f_find()
    find_form.geometry('330x140+200+250')
    Label(find_form, text='替换:').grid(row=1,column=0,sticky='w')
    Entry(find_form,width=20).grid(row=1,column=1,padx=2,pady=2,sticky='we')
    Button(find_form, text='替换').grid(row=1,column=2,padx=2,pady=2,sticky='e'+'w')
    Button(find_form, text='替换全部').grid(row=2,column=2,padx=2,pady=2,sticky='e'+'w')
    find_cancel_button.grid(row=3,column=2,padx=2,pady=2,sticky='e'+'w')
    find_check.grid(row=3,column=0,sticky='w')
    
def f_cursor_positioning():
    
    global text_field
    
    all_row_num = int(text_field.index(END).split('.')[0])-1
    goto_row = goto_entry.get()

    if goto_row.isdigit():
        goto_row = int(goto_entry.get())
        if goto_row > all_row_num or goto_row<1:
            showinfo(title='记事本-跳行', message='行数超过了总行数')
            return
    else:
        showinfo(title='记事本-跳行', message='不能为字符')
        return
    text_field.mark_set('insert', '{}.{}'.format(goto_row,0))
        
def goto_destroy():
    goto_form.destroy()
    

def f_go_to(event=None):
    global goto_entry, goto_form
    goto_form = Toplevel(main_form)
    goto_form.title('转到指定行')
    goto_form.geometry('260x90')
    Label(goto_form, text='行号(L):').grid(row=0,column=0, padx=4,sticky='w')
    goto_entry = Entry(goto_form, width=34)
    goto_entry.grid(row=1,column=0, padx=4)
    goto_entry.focus_set()
    Button(goto_form, text='转到', width=9, height=1, command=f_cursor_positioning).grid(row=2, column=0, pady=10)
    Button(goto_form, text='取消', width=9, height=1, command=goto_destroy).grid(row=2, column=0, pady=10, sticky='e')
    

def f_sel_all(event=None):
    global text_field
    text_field.tag_add('sel', 1.0, END)

def f_date(event=None):
    global text_field
    f_time = time.strftime('%H:%M %Y/%m/%d', time.localtime())
    text_field.insert(INSERT, f_time)

def f_pop_up(event):
    edit_menu.post(event.x_root,event.y_root)

def f_wrap_line():
    pass

def f_font_format():
    pass

def f_status_bar(event=None):
    global main_form, text_field, status_bar
    row_col_num = text_field.index(INSERT).split('.')
    f_status_bar_content = '第{}行，第{}列'.format(row_col_num[0],
                                          int(row_col_num[1])+1)
    status_bar['text'] = f_status_bar_content

def f_view_help():
    showinfo(title='帮助', message='这......需要什么帮助(꒪Д꒪)ノ ？')

def f_about():
    showinfo(title='关于\"记事本\"', message='版本0.1(GUI测试成品) \
             \n允许学习测试，欢迎提交BUG\n尚有数个功能未实现,欢迎提供思路 \
             \n参考于辛星的教程以及搜索引擎\nGithub: https://github.com/hiJordan')

def f_text_changed(event=None):
    global text_changed
    text_changed = True

def direction(event):
    if event.keysym == 'Right':
        f_status_bar()
    elif event.keysym == 'Left':
        f_status_bar()
    elif event.keysym == 'Down':
        f_status_bar()
    elif event.keysym == 'Up':
        f_status_bar()
    elif event.keysym == 'Return':
        f_status_bar()
    elif event.keysym == 'Key':
        f_status_bar()

#global main_form, text_field
file_name = '记事本 - 无标题'
main_form = Tk()
main_form.title(file_name)
main_form.geometry('683x384+100+110') #683x384指窗体的大小,100与110分别指距X与Y轴的间隔

text_changed = False

#设置菜单栏
menu_bar = Menu(main_form)

#文件菜单
file_menu = Menu(main_form, tearoff=False)
file_menu_item_name = ['新建(N)', '打开(O)', '保存(S)', '另存为(A)', '退出(E)']
file_menu_item_shortcut_keys = ['Ctrl+N', 'Ctrl+O', 'Ctrl+S', ' ', ' ']
file_menu_connection_fun = [f_new, f_open, f_save, f_save_as, f_exit]
for name, key, fun in zip(file_menu_item_name, file_menu_item_shortcut_keys,
                          file_menu_connection_fun):
    file_menu.add_command(label=name, accelerator=key, command=fun)

#编辑菜单
edit_menu = Menu(main_form, tearoff=False)
edit_menu_item_name = ['撤销(U)', '剪贴(T)', '复制(C)', '粘贴(P)', '删除(L)',
    '查找(F)', '查找下一个(N)', '替换(R)', '转到(G)', '全选(A)', '时间/日期(D)']
edit_menu_item_shortcut_keys = ['Ctrl+Z', 'Ctrl+X', 'Ctrl+C', 'Ctrl+V', 'Del',
                          'Ctrl+F', 'F3', 'Ctrl+H', 'Ctrl+G', 'Ctrl+A', 'F5']
edit_menu_connection_fun = [f_revoke, f_cut, f_copy, f_paste, f_del, f_find,
                            f_next, f_replace, f_go_to, f_sel_all, f_date]
for name, key, fun in zip(edit_menu_item_name, edit_menu_item_shortcut_keys,
                          edit_menu_connection_fun):
    edit_menu.add_command(label=name, accelerator=key, command=fun)

#格式菜单
format_menu = Menu(main_form, tearoff=False)
format_menu_item_name = ['自动换行(W)', '字体(F)...']
format_menu_connection_fun = [f_wrap_line, f_font_format]
for name, fun in zip(format_menu_item_name, format_menu_connection_fun):
    format_menu.add_command(label=name, command=fun)

#查看菜单
view_menu = Menu(main_form, tearoff=False)
view_menu.add_command(label='状态栏(S)', command=f_status_bar)

#帮助菜单
help_menu = Menu(main_form, tearoff=False)
for name, fun in zip(['查看帮助(H)', '关于记事本(A)'], [f_view_help, f_about]):
    help_menu.add_command(label=name, command=fun)

all_menu = {'文件(F)':file_menu, '编辑(E)':edit_menu, '格式(O)':format_menu,
            '查看(V)':view_menu, '帮助(H)':help_menu}
for name, item in all_menu.items():
    menu_bar.add_cascade(label=name, menu=item)
main_form['menu'] = menu_bar

#文本编辑区
text_field = Text(main_form)
text_scroll = Scrollbar(text_field)
text_field.config(yscrollcommand=text_scroll.set)
text_scroll.config(command=text_field.yview)
text_field.pack(expand=1, fill=BOTH)
text_scroll.pack(side=RIGHT, fill=Y)


status_bar = Label(main_form, anchor='e')
status_bar.pack(side=BOTTOM, fill=X)


#绑定功能函数
text_field.bind('<KeyRelease>', direction)

text_field.bind('<ButtonRelease-1>', f_status_bar)
text_field.bind('<Key>', f_text_changed)
text_field.bind('<Control-N>', f_new)
text_field.bind('<Control-n>', f_new)
text_field.bind('<Control-O>', f_open)
text_field.bind('<Control-o>', f_open)
text_field.bind('<Control-S>', f_save)
text_field.bind('<Control-s>', f_save)
text_field.bind('<Control-F>', f_find)
text_field.bind('<Control-f>', f_find)
text_field.bind('<F3>', f_next)
text_field.bind('<Control-H>', f_replace)
text_field.bind('<Control-h>', f_replace)
text_field.bind('<Control-G>', f_go_to)
text_field.bind('<Control-g>', f_go_to)
text_field.bind('<F5>', f_date)
text_field.bind('<Button-3>', f_pop_up)

main_form.mainloop()




