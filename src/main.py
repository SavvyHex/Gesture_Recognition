import tkinter
import command_controller
import admin

class Home:
    def __init__(self) -> None:
        self.cc = command_controller.CommandController()
        self.root = tkinter.Tk()
        self.root.title("SmartGes")
        self.root.geometry("640x480")
        
        self.buttons()
        
        self.root.mainloop()
        
    def buttons(self):
        self.openCam = tkinter.Button(self.root, text="Open Hand Tracker", command=self.cc.run)
        self.openCam.pack()
        
        self.adminScreen = tkinter.Button(self.root, text="Create A new Command", command=self.admin_screen)
        self.adminScreen.pack()

    def admin_screen(self):
        admin.AdminScreen()
        
if __name__ == "__main__":
    Home()