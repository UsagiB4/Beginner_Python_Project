from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")

def time():
    string=strftime('%H:%M:%S %p')
    lable.config(text=string)
    lable.after(1000, time)

lable = Label(root, font=("connection serif", 80), background ="black", foreground="cyan")
lable.pack(anchor="center")
time()

mainloop()
