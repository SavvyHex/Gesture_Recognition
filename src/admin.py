import tkinter

class AdminScreen:
    def __init__(self) -> None:
        self.root = tkinter.Tk()
        self.root.title("Admin Screen")
        self.root.geometry("640x480")
        
        self.buttons()
        
        self.root.mainloop()
        
    def buttons(self):
        self.submit = tkinter.Button(self.root, text="Submit")