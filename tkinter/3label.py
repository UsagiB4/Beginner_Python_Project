from tkinter import Tk, Label,PhotoImage

myWindow = Tk()

image = PhotoImage(file='jup.png')

# A label is an area widget that holds text, image within a window
myLabel = Label(
                myWindow,
                text="hello world",  # display text
                font=('Arial', 40, 'bold'),  # font style
                fg="cyan",  # foreground color/ text color (you can also use color codes instead of name)
                bg='black',  # background color
                relief='sunken',  # border style  (flat, groove, raised, ridge, solid, or sunken)
                bd=10,  # border width
                padx=20,  # padding x
                pady=50,  # padding y
                image=image,
                compound='center'  # bottom, center, left, none, right, or top
                )
myLabel.pack()  # packing Label to show on the window. Here x and y is coordinate fo the label.


myWindow.mainloop()
