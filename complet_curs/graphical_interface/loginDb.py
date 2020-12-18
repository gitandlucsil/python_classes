from tkinter import *
import mysql.connector

class Login(object):

    def __init__(self, master):
        self.master = master
        self.master.title("Acess to the system")
        Label(self.master, text="User and password").grid(row=1, column=1, columnspan=2)
        Label(self.master, text="User").grid(row=2, column=1)
        # self.user = Entry(self.master, width=15).grid(row=2, column=2)
        self.user = Entry(self.master, width=15)
        self.user.grid(row=2, column=2)
        self.user.focus_force()
        Label(self.master, text="Password").grid(row=3, column=1)
        self.password = Entry(self.master, width=15, show="*", fg="darkgrey")
        self.password.grid(row=3, column=2)
        self.status = Label(self.master, text="Status ...")
        self.status.grid(row=4, column=1, columnspan=2, pady=4)
        self.entry = Button(self.master, width=7, text="Login", command=self.validatePassword)
        self.entry.grid(row=5, column=1, pady=4, padx=3)
        self.exit = Button(self.master, width=7, text="Exit", command=self.leave)
        self.exit.grid(row=5, column=2, pady=4, padx=3)

    def validatePassword(self):
        if self.user.get() == "andre" and self.password.get() == "lucas":
            self.status['text'] = "Acess Aproved!"
        else:
            self.status['text'] = "Acess Reproved!"

    def leave(self):
        self.master.destroy()

root = Tk()
Login(root)
root.mainloop()