from tkinter import *

root = Tk()
root.title('Simple Calculator')

inputBox = Entry(root, width=35, borderwidth=5)


def numBtn(num):
    inputBox.insert(1, num)


btn1 = Button(root, text='1', padx=25, pady=25, command=lambda: numBtn(1))
btn2 = Button(root, text='2', padx=25, pady=25, command=lambda: numBtn(2))
btn3 = Button(root, text='3', padx=25, pady=25, command=lambda: numBtn(3))
btn4 = Button(root, text='4', padx=25, pady=25, command=lambda: numBtn(4))
btn5 = Button(root, text='5', padx=25, pady=25, command=lambda: numBtn(5))
btn6 = Button(root, text='6', padx=25, pady=25, command=lambda: numBtn(6))
btn7 = Button(root, text='7', padx=25, pady=25, command=lambda: numBtn(7))
btn8 = Button(root, text='8', padx=25, pady=25, command=lambda: numBtn(8))
btn9 = Button(root, text='9', padx=25, pady=25, command=lambda: numBtn(9))
btn0 = Button(root, text='0', padx=25, pady=25, command=lambda: numBtn(0))
btnAdd = Button(root, text='+', padx=25, pady=25, command=lambda: numBtn())
btnSub = Button(root, text='-', padx=25, pady=25, command=lambda: numBtn())
btnClr = Button(root, text='C', padx=25, pady=25, command=lambda: numBtn())
btnEq = Button(root, text='=', padx=25, pady=25, command=lambda: numBtn())

inputBox.grid(row=5, column=0, columnspan=3)
btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)
btn0.grid(row=3, column=0)
btnAdd.grid(row=3, column=1)
btnSub.grid(row=3, column=2)
btnEq.grid(row=4, column=0)
btnClr.grid(row=4, column=1)

root.mainloop()
