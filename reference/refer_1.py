# FishNotepad
# 无名侠
# 2015.7.7
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os
def ReadFile(filename):
    '加载文件'
    fp=open(filename,'r')
    for iter1 in fp:
        yield iter1
    fp.close()
    return
def WriteFile(filename,data):
    fp=open(filename,'w')
    fp.write(data)
    fp.close()
class commands:
    g_openfile = ''
    g_bChange = False
    def __init__(self,tkapp,theText):
        self.app=tkapp
        self.text=theText
    def cm_open(self,e=0):
        'COMMAND 打开'
        if self.g_bChange:
            if not askyesno(message='文件未保存:'+self.g_openfile+' 是否继续打开新文件?'):
                return
        self.g_openfile=askopenfilename()
        if self.g_openfile == '':
            return
        try:
            mainEdit.delete(1.0, END)
            for str1 in ReadFile(self.g_openfile):
                mainEdit.insert(END,str1)
        except IOError:
            showerror(message='无法打开文件:'+self.g_openfile)
            return
        self.app.title('记事本 - '+self.g_openfile)
    def cm_new(self,e=0):
        'COMMAND 新建'
        if self.g_bChange:
            if not askyesno(message='文件未保存:'+self.g_openfile+' 是否继续创建新文件?', title='?'):
                return
        mainEdit.delete(1.0,END)
        self.g_openfile=''
        self.b_bChange = False
        self.app.title('记事本')
        
    def cm_save(self,e=0):
        if  not self.g_bChange:
            return
        if self.g_openfile=='':
            self.cm_save2()
        else:
            try:
                WriteFile(self.g_openfile,mainEdit.get(1.0,END))
            except IOError:
                showerror(message='无法写文件:'+self.g_openfile)
                return
            self.g_bChange = False
    def cm_save2(self):
        'COMMAND 另存为'
        tmp = asksaveasfilename()
        if tmp=='':
            return
        try:
            WriteFile(tmp,mainEdit.get(1.0,END))
        except IOError:
            showerror(message='无法写文件:'+tmp)
            return
        self.app.title('记事本 - '+tmp)
        self.g_openfile = tmp
        self.g_bChange  = False
    def cm_change(self,e):
        self.g_bChange = True
        self.text.edit_separator()

#创建主框架
theApp=Tk()
theApp.title('记事本')
sb=Scrollbar(theApp)
#创建Text 组件
mainEdit = Text(theApp,yscrollcommand=sb.set,autoseparators=False, undo=True)
cm=commands(theApp,mainEdit)
mainEdit.grid(row=0,column=0,sticky=N+S+W+E)
#绑定事件
mainEdit.bind('<Key>',cm.cm_change) #文档内容被修改
mainEdit.bind('<Control-Key-n>',cm.cm_new)
mainEdit.bind('<Control-Key-s>',cm.cm_save)
mainEdit.bind('<Control-Key-o>',cm.cm_open)
#创建滚动条
sb.grid(row=0,column=1,sticky=N+S)
sb.config(command=mainEdit.yview)
#创建菜单
mbar = Menu(theApp) #菜单条
#文件菜单
filemenu=Menu(mbar,tearoff=False)
filemenu.add_command(label='新建 Ctrl+N',command=cm.cm_new)
filemenu.add_command(label='打开 Ctrl+O',command=cm.cm_open)
filemenu.add_command(label='保存 Ctrl+S',command=cm.cm_save)
filemenu.add_command(label='另存为',command=cm.cm_save2)
filemenu.add_separator()
filemenu.add_command(label='退出',command=theApp.quit)
#编辑菜单
editmenu=Menu(mbar,tearoff=False)
editmenu.add_command(label='撤销 Ctrl+Z',command=mainEdit.edit_undo)
editmenu.add_separator()
editmenu.add_command(label='复制 Ctrl+C')
editmenu.add_command(label='粘贴 Ctrl+V')
editmenu.add_separator()
editmenu.add_command(label='查找')
editmenu.add_command(label='查找下一个')
editmenu.add_separator()
editmenu.add_command(label='替换')
#帮助菜单
helpmenu = Menu(mbar,tearoff=False)
helpmenu.add_command(label='--- 感谢使用 ---')
helpmenu.add_command(label='By 无名侠')
helpmenu.add_command(label='www.pandaos.net')
helpmenu.add_command(label='bbs.fishc.com')
#附加
mbar.add_cascade(label='文件',menu=filemenu)
mbar.add_cascade(label='编辑',menu=editmenu)
mbar.add_cascade(label='关于',menu=helpmenu)
theApp.config(menu=mbar)
mainloop()
