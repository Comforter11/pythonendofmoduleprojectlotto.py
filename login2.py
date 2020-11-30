# COMFORTER MAKWEYA CLASS-2
from tkinter import *
from tkinter import messagebox as mb
from random import sample
import random
from tkinter import messagebox

window1 = Tk()

window1.title("LOTTO LOGIN")
window1.geometry("700x300")
window1.configure(bg='Yellow')

img = Canvas(window1, width=5000, height=2000)

img.place(x=-20, y=-20)
_img1 = PhotoImage(file="output.png")
img.create_image(20, 20, anchor=NW, image=_img1)


def check():
    age = int(entry3.get())
    ages = age

    if ages < 18:
        mb.showwarning("Warning", "Under Age!")
    else:
        mb.showinfo("Success", "Go through!")
        window1.destroy()
        import result
        result.verify()


label3 = Label(window1, text=" No Under 18's/Winners know when to stop!!!-- @Play-Lotto!", bg='blue', font=('Helvetica', 16, 'bold'))
label3.grid(row=1, column=0)


button1 = Button(window1, text="Submit", command=check, font=('Helvetica', 14, 'bold'))

label1 = Label(window1, text="Name: ", font=('Helvetica', 14, 'bold'))
entry1 = Entry(window1)

label2 = Label(window1, text="Surname:", font=('Helvetica', 14, 'bold'))
entry2 = Entry(window1)

label3 = Label(window1, text="Age:", font=('Helvetica', 14, 'bold'))
entry3 = Entry(window1)

label1.place(x=0, y=50)
label2.place(x=0, y=100)
label3.place(x=0, y=150)

entry1.place(x=150, y=50)
entry2.place(x=150, y=100)
entry3.place(x=150, y=150)
button1.place(x=200, y=200)

window1.mainloop()
