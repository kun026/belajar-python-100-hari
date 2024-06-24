# from tkinter import *
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(500, 300)

# Label
my_label = tkinter.Label(text="New Label", font=("Arial", 24, "bold"))
my_label.pack()

# Change label text
my_label["text"] = "Prof. Dr. Ridho Syam"
my_label.config(text="I hope tomorrow I am rich")

# Button
def btn_click():
    # print("I got Clicked")
    # my_label["text"] = "Button got clicked"
    my_label.config(text=form.get())
    


btn1 = tkinter.Button(text="Click Me", command=btn_click)
btn1.pack()

# Entry
form = tkinter.Entry(width=25)
form.pack()

window.mainloop()
