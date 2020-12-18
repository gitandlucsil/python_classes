from tkinter import *
import tkinter.messagebox

class App(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.buttons()

    def buttons(self):
        self.button7 = Button(self,text="7",fg="Black",bg="Yellow",width=6,height=2)
        self.button7.grid(row="1",column="1")
        self.button8 = Button(self,text="8",fg="Black",bg="Yellow",width=6,height=2)
        self.button8.grid(row="1",column="2")
        self.button9 = Button(self,text="9",fg="Black",bg="Yellow",width=6,height=2)
        self.button9.grid(row="1",column="3")
        self.buttonSum = Button(self,text="+",fg="Black",bg="Yellow",width=6,height=2)
        self.buttonSum.grid(row="1",column="4")

        self.button4 = Button(self,text="4",fg="Black",bg="Yellow",width=6,height=2)
        self.button4.grid(row="2",column="1")
        self.button5 = Button(self,text="5",fg="Black",bg="Yellow",width=6,height=2)
        self.button5.grid(row="2",column="2")
        self.button6 = Button(self,text="6",fg="Black",bg="Yellow",width=6,height=2)
        self.button6.grid(row="2",column="3")
        self.buttonMul = Button(self,text="*",fg="Black",bg="Yellow",width=6,height=2)
        self.buttonMul.grid(row="2",column="4")

        self.button1 = Button(self,text="1",fg="Black",bg="Yellow",width=6,height=2)
        self.button1.grid(row="3",column="1")
        self.button2 = Button(self,text="2",fg="Black",bg="Yellow",width=6,height=2)
        self.button2.grid(row="3",column="2")
        self.button3 = Button(self,text="3",fg="Black",bg="Yellow",width=6,height=2)
        self.button3.grid(row="3",column="3")
        self.buttonMin = Button(self,text="-",fg="Black",bg="Yellow",width=6,height=2)
        self.buttonMin.grid(row="3",column="4")

        self.button0 = Button(self,text="0",fg="Black",bg="Yellow",width=6,height=2)
        self.button0.grid(row="4",column="1")
        self.buttonCE = Button(self,text="CE",fg="Black",bg="Yellow",width=6,height=2)
        self.buttonCE.grid(row="4",column="2")
        self.buttonEqual = Button(self,text="=",fg="Black",bg="Yellow",width=6,height=2)
        self.buttonEqual.grid(row="4",column="3")
        self.buttonDiv = Button(self,text="/",fg="Black",bg="Yellow",width=6,height=2)
        self.buttonDiv.grid(row="4",column="4")

myApp = App()
myApp.master.title("Test window!")
myApp.master.maxsize(1024,768)
myApp.master.mainloop() 