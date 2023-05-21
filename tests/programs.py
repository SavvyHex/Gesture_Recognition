import tkinter
from tkinter import *

#Home page
home=Tk()
Label=Label(home,text='SmartGes',fg='Black',bg='lightsteelblue',font=('Inkfree',35))
Label.place(x=200,y=50)
btn=Button(home,text='Login',bg='steelblue',fg='Black',width=30)
btn.place(x=200,y=200)
btn2=Button(home,text='Admin',fg='Black',bg='steelblue',width=30)
btn2.place(x=200,y=240)
home.title('Home')
home.geometry("700x400")
home.configure(bg='lightsteelblue')
home.mainloop()

#Login page
login=Tk()
login.title('Login')
login.geometry('350x100')
login.configure(bg='lightsteelblue')
na=tkinter.Entry(login)
na.grid(row=1,column=2)
un=tkinter.Entry(login)
un.grid(row=2,column=2)
ps=tkinter.Entry(login,show="*")
ps.grid(row=3,column=2)
sb=tkinter.Button(login,text='Submit')
sb.grid(row=4,column=5)
nalabel=tkinter.Label(login,text='Name:',bg='lightsteelblue')
nalabel.grid(row=1,column=1)
unlabel=tkinter.Label(login,text='Username:',bg='lightsteelblue')
unlabel.grid(row=2,column=1)
pslabel=tkinter.Label(login,text='Password:',bg='lightsteelblue')
pslabel.grid(row=3,column=1)


#Admin page
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













