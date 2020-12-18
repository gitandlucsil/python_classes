from tkinter import *
import tkinter.messagebox

class App(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.components()

    def components(self): 
        self.edit = Entry(self.master, width=37)
        self.edit.grid(row=1, column=0)
        buttons = ["7","8","9","+","4","5","6","*","1","2","3","-","0","CE","=","/"]
        row = 1
        col = 1
        for button in buttons:
            cmd = lambda bt = button:self.process(bt)
            self.but = Button(self, text=button, width=6, height=2, command=cmd)
            self.but.grid(row=row, column=col)
            col += 1
            if col > 4:
                col = 1
                row += 1

    def process(self, button):
        if button == "=":
            try:
                calc = eval(self.edit.get())
                self.edit.insert(END, "="+str(calc))
            except:
                self.edit.insert(END, "Error")
        elif button == "CE":
            self.edit.delete(0, END)
        else:
            if "=" in self.edit.get():
                self.edit.delete(0, END)
            self.edit.insert(END, button)
        
myApp = App()
myApp.master.title("Test window!")
myApp.master.maxsize(1024,768)
myApp.master.mainloop() 