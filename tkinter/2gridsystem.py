from tkinter import *

root = Tk()

myLabel1 = Label(root, text="My Program")
myLabel2 = Label(root, text="Your Program")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=2, column=2)

root.mainloop()

