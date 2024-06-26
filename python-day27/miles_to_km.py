import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.geometry("200x100")
window.config(padx=20, pady=20)


def convert_km():
    miles = int(input_miles.get())
    km = round(miles * 1.609)
    result_convert.config(text=f"{km}")


input_miles = tkinter.Entry(width=10)
input_miles.insert(tkinter.END, string=0)
input_miles.focus()
input_miles.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

equel_label = tkinter.Label(text="is equal to")
equel_label.grid(column=0, row=1)

result_convert = tkinter.Label(text=0)
result_convert.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

calc_btn = tkinter.Button(text="Calculate", 
                          command=convert_km)
calc_btn.grid(column=1, row=2)



window.mainloop()