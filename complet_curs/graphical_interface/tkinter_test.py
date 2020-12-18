from tkinter import *
import tkinter.messagebox

class App(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.buttons()
        self.labels()
        self.dataentry()

    def buttons(self):
        self.button = Button(self)
        self.button["text"] = "Welcome to Python!"
        self.button["command"] = self.actionPrint
        self.button["font"] = ("Arial","16","bold")
        self.button["height"] = 2
        self.button["width"] = 40
        self.button.pack(side="top")

        self.button2 = Button(self,text="Second Button",fg="Blue",bg="Red")
        self.button2.pack(side="bottom")
        
        self.buttonExit = Button(self,text="Exit",fg="red",bg="blue",command=self.destroy)
        self.buttonExit.pack(side="bottom")

    def labels(self):
        self.label = Label(self,text="Second Button",fg="Black",bg="Yellow")
        self.label.pack(side="top")

    def dataentry(self):
        self.edit = Entry(self)
        self.edit.pack(side="top")

    def actionPrint(self):
        print("Action executed!")
        print(self.edit.get())
        tkinter.messagebox.showinfo(title="Message",message="This is a message box!")

myApp = App()
myApp.master.title("Test window!")
myApp.master.maxsize(1024,768)
myApp.master.geometry("800x600")
myApp.master.mainloop()