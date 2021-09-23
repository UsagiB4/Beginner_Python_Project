from tkinter import *

# difference between window and widgets
# window works as a container for widgets. It is an certain area that contains the widgets.
#__________________________________________________
# widgets are GUI elements. Such as, Button, textbox, labels, images and so on.


window = Tk()  # creating an window

window.geometry("560x360")  # it will give window the height and the width. _.geometry("WxH")
window.title("My window")  # set a title of the window.

# Setting an icon for the window.
# tkinter can not use regular image as icon. so you have to convert it into a usable format.
icon = PhotoImage(file='icon.png')  # this will convert our image.
window.iconphoto(True, icon)  # Setting the icon to window.

# changing the color of the window.
window.config(backgroun="cyan")  # changing the window color into cyan

window.mainloop()  # This will display the window.
