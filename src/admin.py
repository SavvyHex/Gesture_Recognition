import tkinter

class AdminScreen:
    def __init__(self) -> None:
        self.colours = {"eggplant" : "#6C464F", 
                        "mb pink" : "#9E768F", 
                        "cool gray" : "#9FA4C4", 
                        "light blue": "#B3CDD1"
                    }
        
        self.root = tkinter.Tk()
        self.root.title("Admin Screen")
        self.root.geometry("640x480")
        self.root.configure(bg=self.colours["cool gray"])
        
        self.buttons()
        
        self.root.mainloop()
        
    def buttons(self):
        self.submit = tkinter.Button(self.root, text="Submit")
        
if __name__ == "__main__":
    AdminScreen()