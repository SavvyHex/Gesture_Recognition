from tkinter import *
import forms

class Home():
    def __init__(self) -> None:
        self.root=Tk()
        title=Label(self.root,text='SmartGes',fg='Black',bg='lightsteelblue',font=('Inkfree',35))
        title.place(x=200,y=50)
        btn=Button(self.root,text='Login',bg='steelblue',fg='Black',width=30)
        btn.place(x=200,y=200)
        btn2=Button(self.root,text='Register',fg='Black',bg='steelblue',width=30)
        btn2.place(x=200,y=240)
        self.root.title('Home')
        self.root.geometry("700x400")
        self.root.configure(bg='lightsteelblue')
        self.root.mainloop()
    
    def register(self):
        self.root.destroy()
        forms.Registration()
        
    def login(self):
        self.root.destroy()
        forms.Login()

if __name__ == "__main__":
    Home()