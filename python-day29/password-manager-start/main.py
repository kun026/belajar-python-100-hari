import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    lett = [random.choice(letters) for _ in range(random.randint(8, 10))]
    num = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    sym = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list = [*lett, *num, *sym]
    random.shuffle(password_list)
    pw = "".join(password_list)
    input_password.delete(0, tk.END)
    input_password.insert(0, pw)
    pyperclip.copy(pw)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input_website.get()
    email = input_email_username.get()
    password = input_password.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        message = f"These are details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?"
        is_ok = messagebox.askokcancel(title=website, message=message)
        if is_ok:
            with open("./data.txt", mode="a") as data:
                data.write(f"{website} | {email} | {password}\n")
            
            input_website.delete(0, tk.END)
            input_email_username.delete(0, tk.END)
            input_email_username.insert(0, "@gmail.com")
            input_password.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.title("Password Manager")
root.config(padx=50, pady=50)

logo = tk.PhotoImage(file="./logo.png")
canvas = tk.Canvas(root, width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = tk.Label(root, text="Website:")
website_label.grid(row=1, column=0)

email_username = tk.Label(root, text="Email/Username:")
email_username.grid(row=2, column=0)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=3, column=0)

input_website = tk.Entry(root, width=40)
input_website.focus()
input_website.grid(row=1, column=1, columnspan=2)

input_email_username = tk.Entry(root, width=40)
input_email_username.insert(0, "@gmail.com")
input_email_username.grid(row=2, column=1, columnspan=2)

input_password = tk.Entry(root, width=22)
input_password.grid(row=3, column=1)

btn_add = tk.Button(root, text="Add", width=34, command=save)
btn_add.grid(row=4, column=1, columnspan=2)

btn_generate_pass = tk.Button(root, text="Generate Password", command=generate_password)
btn_generate_pass.grid(row=3, column=2)



root.mainloop()
