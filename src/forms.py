import tkinter

class Login:
    def __init__(self, bgcol) -> None:
        self.bgcol = bgcol
        self.root = tkinter.Tk()
        self.root.title("Login Screen")
        self.root.configure(bg=self.bgcol)
        
        self.labels()
        self.inputs()
        
        self.root.mainloop()
        
    def inputs(self):
        self.unameText = tkinter.Entry(self.root)
        self.unameText.grid(row=1, column=2)
        
        self.passText = tkinter.Entry(self.root, show="*")
        self.passText.grid(row=2, column=2)
        
        self.submit = tkinter.Button(self.root, text="Submit", command=self.submit)
        self.submit.grid(row=3, column=2)
        
    def labels(self):
        self.unameLabel = tkinter.Label(self.root, text="Username : ", bg=self.bgcol)
        self.unameLabel.grid(row=1, column=1)
        
        self.passLabel = tkinter.Label(self.root, text="Password : ", bg=self.bgcol)
        self.passLabel.grid(row=2, column=1)
        
    def submit(self):
        from main import Home
        
        self.name = self.unameText.get()
        self.passwd = self.passText.get()
        
        self.root.destroy()
        Home(self.name=="admin")
        
if __name__ == "__main__":
    Login("white")
