import tkinter
from tkinter import *
class admin:
    admin=Tk()
    admin.title('Admin')
    admin.geometry('350x90')
    admin.configure(bg='lightsteelblue')
    admin.mainloop
    un=tkinter.Entry(admin)
    un.grid(row=2,column=2)
    ps=tkinter.Entry(admin,show="*")
    ps.grid(row=3,column=2)
    sb=tkinter.Button(admin,text='Submit')
    sb.grid(row=4,column=5)
    unlabel=tkinter.Label(admin,text='Username:',bg='lightsteelblue')
    unlabel.grid(row=2,column=1)
    pslabel=tkinter.Label(admin,text='Password:',bg='lightsteelblue')
    pslabel.grid(row=3,column=1)
