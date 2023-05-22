import tkinter
import tkinter.messagebox
import mysql.connector

class AdminScreen:
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(user="saketh", password="notpassword", host="localhost", database="smartges")
        self.cursor = self.connection.cursor()

        self.colours = {
            "eggplant": "#6C464F", 
            "mb pink": "#9E768F", 
            "cool gray": "#9FA4C4", 
            "light blue": "#B3CDD1"
        }
        
        self.root = tkinter.Tk()
        self.root.title("Admin Screen")
        self.root.geometry("640x480")
        self.root.configure(bg=self.colours["cool gray"])

        self.title = tkinter.Label(self.root, text="Command Creation", bg=self.colours["cool gray"], font=("Helvetica", 28))
        self.title.place(x=160, y=50)

        self.code_label = tkinter.Label(self.root, text="Code:", bg=self.colours["cool gray"], font=("Helvetica", 16))
        self.code_label.place(x=50, y=220)

        self.code_entry = tkinter.Entry(self.root, width=10, font=("Helvetica", 16))
        self.code_entry.place(x=120, y=220)

        self.file_label = tkinter.Label(self.root, text="File Name:", bg=self.colours["cool gray"], font=("Helvetica", 16))
        self.file_label.place(x=50, y=280)

        self.file_name = tkinter.Entry(self.root, font=("Helvetica", 16))
        self.file_name.place(x=170, y=280)

        self.submit = tkinter.Button(self.root, text="Submit", command=self.submit)
        self.submit.place(x=300, y=400)

        self.root.mainloop()
        
    def submit(self):
        code = self.code_entry.get()
        file = self.file_name.get()

        if len(code) != 5:
            tkinter.messagebox.showerror("Invalid Code", "Please enter a five-digit code.")
            return
        for d in code:
            if d not in '10':
                tkinter.messagebox.showerror("Invalid Code", "All digits must be either 0 or 1.")
                return

        self.cursor.execute(f"INSERT INTO gestures VALUES ('{code}', '{file}')")
        self.connection.commit()

        self.cursor.close()
        self.connection.close()

        self.root.destroy()
        tkinter.messagebox.showinfo("Database Updated", "Database Successfully Updated")
        
if __name__ == "__main__":
    AdminScreen()
