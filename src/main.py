import tkinter
import tkinter.messagebox

import command_controller
import admin
import home

class Home:
    def __init__(self, admin=False) -> None:
        
        self.colours = {"eggplant" : "#6C464F", 
                        "mb pink" : "#9E768F", 
                        "cool gray" : "#9FA4C4", 
                        "light blue": "#B3CDD1"
                    }
        
        self.isAdmin = admin
        
        self.cc = command_controller.CommandController()
        self.root = tkinter.Tk()
        self.root.title("SmartGes")
        self.root.geometry("640x480")
        self.root.configure(bg=self.colours["eggplant"])
        
        self.labels()
        self.buttons()
        
        self.root.mainloop()
        
    def labels(self):
        self.mainLabel = tkinter.Label(self.root, text="SmartGes", bg=self.colours["eggplant"], font=("Helvetica", 32))
        self.mainLabel.place(x=220, y=50)
        
    def buttons(self):
        self.openCam = tkinter.Button(self.root, text="Open Hand Tracker", command=self.cc.run, width=25)
        self.openCam.place(x=200, y=180)
        
        self.adminScreen = tkinter.Button(self.root, text="Create A new Command", command=self.admin_screen, width=25)
        self.adminScreen.place(x=200, y=240)

        self.volcnt = tkinter.Button(self.root, text="Volume Control", command=self.volc, width=25)
        self.volcnt.place(x=200, y=300)

        self.virt= tkinter.Button(self.root, text="Virtual Mouse", command=self.virtual, width=25)
        self.virt.place(x=200,y=360)

    def admin_screen(self):
        if self.isAdmin:
            admin.AdminScreen()
        else:
            tkinter.messagebox.showinfo("Error", "You need to be an admin")

    def volc(self):
        import volctrl
    
    def virtual(self):
        import v_m

    
        
if __name__ == "__main__":
    home.Home()
