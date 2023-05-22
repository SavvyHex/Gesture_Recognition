import tkinter
from tkinter import *

class home:
    home=Tk()
    Label=Label(home,text='SmartGes',fg='Black',bg='lightsteelblue',font=('Inkfree',35))
    Label.place(x=200,y=50)
    btn=Button(home,text='Login',bg='steelblue',fg='Black',width=30)
    btn.place(x=200,y=200)
    btn2=Button(home,text='Admin',fg='Black',bg='steelblue',width=30)
    btn2.place(x=200,y=240)
    btn3=Button(home,text='Signup',bg='steelblue',fg='black',width=30)
    btn3.place(x=200,y=280)
    home.title('Home')
    home.geometry("700x400")
    home.configure(bg='lightsteelblue')
    home.mainloop()

