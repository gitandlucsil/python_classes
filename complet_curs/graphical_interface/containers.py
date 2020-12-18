from tkinter import *
import tkinter.messagebox

class Containers:

    def __init__(self, master):
        self.container1 = Frame(master)
        self.container2 = Frame(master)
        self.container3 = Frame(master)
        self.containerseparator = Frame(master, height=20)
        self.container1.pack()
        self.container2.pack()
        self.containerseparator.pack()
        self.container3.pack()
        Button(self.container1, text="Button 1").pack(side=RIGHT)
        Button(self.container2, text="Button 2").pack(side=LEFT)
        Button(self.container3, text="Button 3").pack()
        Button(self.container3, text="Button 4 - Exit", command=self.close).pack(side=RIGHT)

    def close(self):
        if tkinter.messagebox.askyesno("Do you want to leave?"):
            exit()

def leave():
    pass

root = Tk()
root.protocol("WM_DELETE_WINDOW", leave)
Containers(root)
root.maxsize(1024,768)
root.geometry("800x600")
root.mainloop() 