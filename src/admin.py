import tkinter
import tkinter.messagebox
import mysql.connector

class AdminScreen:
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(user="saketh", password="notpassword", host="localhost", database="smartges")
        self.cursor = self.connection.cursor()

        self.colours = {"eggplant" : "#6C464F", 
                        "mb pink" : "#9E768F", 
                        "cool gray" : "#9FA4C4", 
                        "light blue": "#B3CDD1"
                    }
        
        self.root = tkinter.Tk()
        self.root.title("Admin Screen")
        self.root.geometry("640x480")
        self.root.configure(bg=self.colours["cool gray"])

        self.thumb = tkinter.BooleanVar()
        self.index = tkinter.BooleanVar()
        self.middle = tkinter.BooleanVar()
        self.ring = tkinter.BooleanVar()
        self.pinky = tkinter.BooleanVar()
        
        self.labels()
        self.textbox()
        self.buttons()
        
        self.root.mainloop()
        
    def labels(self):
        self.title = tkinter.Label(self.root, text="Command Creation", bg=self.colours["cool gray"], font=("Helvetica", 28))
        self.title.place(x=150, y=50)

        self.file_name = tkinter.Label(self.root, text="File Name : ", bg=self.colours["cool gray"], font=("Helvetica", 18))
        self.file_name.place(x=10, y=130)

        self.checkbox_title = tkinter.Label(self.root, text="Check the boxes for the respective finger to be opened", bg=self.colours["cool gray"], font=("Helvetica", 14))
        self.checkbox_title.place(x=40, y=180)

    def textbox(self):
        self.fileName = tkinter.Entry(self.root)
        self.fileName.place(x=150, y=138)

    def buttons(self):
        self.submit = tkinter.Button(self.root, text="Submit", command=self.submit)
        self.submit.place(x=300, y=400)

        self.thumbButton = tkinter.Checkbutton(self.root, text="Thumb", bg=self.colours["cool gray"], font=("Helvetica", 16), variable=self.thumb).place(x=50, y=220)
        self.indexButton = tkinter.Checkbutton(self.root, text="Index", bg=self.colours["cool gray"], font=("Helvetica", 16), variable=self.index).place(x=50, y=260)
        self.middleButton = tkinter.Checkbutton(self.root, text="Middle", bg=self.colours["cool gray"], font=("Helvetica", 16), variable=self.middle).place(x=50, y=300)
        self.ringButton = tkinter.Checkbutton(self.root, text="Ring", bg=self.colours["cool gray"], font=("Helvetica", 16), variable=self.ring).place(x=50, y=340)
        self.pinkyButton = tkinter.Checkbutton(self.root, text="Pinky", bg=self.colours["cool gray"], font=("Helvetica", 16), variable=self.pinky).place(x=50, y=380)

    def submit(self):
        self.code = f"{1 if self.thumb else 0}{1 if self.index else 0}{1 if self.middle else 0}{1 if self.ring else 0}{1 if self.pinky else 0}"

        self.file = self.fileName.get()
        self.cursor.execute(f"insert into gestures values('{self.code}', '{self.file}')")

        self.connection.commit()

        self.cursor.close()
        self.connection.close()

        self.root.destroy()
        tkinter.messagebox.Message(self.root, message="Database Successfully Updated")
        
if __name__ == "__main__":
    AdminScreen()