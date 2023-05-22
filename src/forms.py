import mysql.connector
import tkinter

class Login:
    def __init__(self, bgcol="lightsteelblue") -> None:
        self.connection = mysql.connector.connect(user="saketh", password="notpassword", host="localhost", database="smartges")
        self.cursor = self.connection.cursor()

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

    def validate(self):
        self.cursor.execute("select * from users")

        rows = self.cursor.fetchall()
        for row in rows:
            if self.name == row[0] and self.passwd == row[1]:
                return True
        return False
        
    def submit(self):
        from main import Home
        
        self.name = self.unameText.get()
        self.passwd = self.passText.get()

        if self.validate():
            self.connection.close()
            self.root.destroy()
            Home(self.name=="admin")
        else:
            tkinter.messagebox.showinfo("Error", "Please check your credentials")
        
class Registration:
    def __init__(self, bgcol="lightsteelblue") -> None:
        self.connection = mysql.connector.connect(user="saketh", password="notpassword", host="localhost", database="smartges")
        self.cursor = self.connection.cursor()

        self.bgcol = bgcol
        self.root = tkinter.Tk()
        self.root.title("Signup Screen")
        self.root.configure(bg=self.bgcol)
        
        self.labels()
        self.inputs()
        
        self.root.mainloop()
        
    def inputs(self):
        self.unameText = tkinter.Entry(self.root)
        self.unameText.grid(row=1, column=2)
        
        self.passText = tkinter.Entry(self.root, show="*")
        self.passText.grid(row=2, column=2)
        
        self.pass2Text = tkinter.Entry(self.root, show="*")
        self.pass2Text.grid(row=3, column=2)
        
        self.submit = tkinter.Button(self.root, text="Submit", command=self.submit)
        self.submit.grid(row=4, column=2)
        
    def labels(self):
        self.unameLabel = tkinter.Label(self.root, text="Username : ", bg=self.bgcol)
        self.unameLabel.grid(row=1, column=1)
        
        self.passLabel = tkinter.Label(self.root, text="Password : ", bg=self.bgcol)
        self.passLabel.grid(row=2, column=1)
        
        self.pass2Label = tkinter.Label(self.root, text="Confirm Password : ", bg=self.bgcol)
        self.pass2Label.grid(row=3, column=1)

    def validate(self):
        if self.passwd != self.pass2wd:
            return 1
        
        self.cursor.execute("select * from users")

        rows = self.cursor.fetchall()
        for row in rows:
            if self.name == row[0]:
                return 2
        return 0
        
    def submit(self):
        from main import Home
        
        self.name = self.unameText.get()
        self.passwd = self.passText.get()
        self.pass2wd = self.pass2Text.get()

        out = self.validate()
        
        if not out:
            self.connection.close()
            self.root.destroy()
            Home(False)
        elif out == 1:
            tkinter.messagebox.showinfo("Error", "The passwords do not match")
        elif out == 2:
            tkinter.messagebox.showinfo("Error", "The username already exists, please log in")