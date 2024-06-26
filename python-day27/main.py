# from tkinter import *
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(500, 300)
window.config(padx=20, pady=20)

"""
pack()
place(x=0, y=0)
grid(column=0, row=0)
"""

# Label
my_label = tkinter.Label(text="New Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

# Change label text
my_label["text"] = "Prof. Dr. Ridho Syam"
my_label.config(text="Rawwrrr")

# Button
def btn_click():
    # print("I got Clicked")
    # my_label["text"] = "Button got clicked"
    my_label.config(text=form.get())
    


btn1 = tkinter.Button(text="Click Me", command=btn_click,)
btn1.grid(column=1, row=1)

btn2 = tkinter.Button(text="New Button", command=btn_click)
btn2.grid(column=2, row=0)

# Entry
form = tkinter.Entry(width=25)
form.grid(column=3, row=2)

window.mainloop()
