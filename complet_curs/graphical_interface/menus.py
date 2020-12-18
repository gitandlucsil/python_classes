from tkinter import *
import tkinter.messagebox

class App(Frame):

    def __init__(self, master ):
        Frame.__init__(self, master)
        self.pack()
        self.menu = Menu(master)
        self.menufile = Menu(self.menu)
        self.menufile.add_command(label="Register Clients",command=self.registerClient)
        self.menufile.add_command(label="Register Customers",command=self.registerCostumer)
        self.menu.add_cascade(label="Register", menu=self.menufile)
        self.menusearch = Menu(self.menu)
        self.menusearch.add_command(label="Search Clients",command=self.searchClient)
        self.menusearch.add_command(label="Search Customers",command=self.searchCostumer)
        self.menu.add_cascade(label="Search", menu=self.menusearch)
        master.config(menu=self.menu)
        #self.grid()

    def registerClient(self):
        print("clicked on register client")

    def registerCostumer(self):
        print("clicked on register costumer")

    def searchClient(self):
        print("clicked on search client")

    def searchCostumer(self):
        print("clicked on search costumer")

root = Tk()
myApp = App(root)
root.title("Test window!")
root.maxsize(1024,768)
root.geometry("800x600")
root.mainloop() 