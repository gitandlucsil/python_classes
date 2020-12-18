from tkinter import *
import tkinter.messagebox

class App(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.buttons()

    def buttons(self):
        self.button2 = Button(self,text="First Button",fg="Blue",bg="Red")
        self.button2.grid(row="1",column="1")
        self.button2 = Button(self,text="Second Button",fg="Blue",bg="Red")
        self.button2.grid(row="1",column="2")
        self.button2 = Button(self,text="Third Button",fg="Blue",bg="Red")
        self.button2.grid(row="2",column="1")
        self.button2 = Button(self,text="Fourth Button",fg="Blue",bg="Red")
        self.button2.grid(row="2",column="2")
        
myApp = App()
myApp.master.title("Test window!")
myApp.master.maxsize(1024,768)
myApp.master.geometry("800x600")
myApp.master.mainloop()