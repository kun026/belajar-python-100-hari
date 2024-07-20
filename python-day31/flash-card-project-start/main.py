import tkinter as tk
import pandas
import random

WORD_DATA = "data/english_words.csv"
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(WORD_DATA)
    # print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    root.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    country = [key for key in current_card]
    canvas.itemconfig(card_title, text=country[0], fill="black")
    canvas.itemconfig(card_word, text=current_card[country[0]], fill="black")
    canvas.itemconfig(card_container, image=card_front)
    flip_timer = root.after(3000, func=flip_card)


def flip_card():
    country = [key for key in current_card]
    canvas.itemconfig(card_title, text=country[1], fill="white")
    canvas.itemconfig(card_word, text=current_card[country[1]], fill="white")
    canvas.itemconfig(card_container, image=card_back)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.title("Flashy")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = root.after(3000, func=flip_card)

card_back = tk.PhotoImage(file="images/card_back.png")
card_front = tk.PhotoImage(file="images/card_front.png")

canvas = tk.Canvas(root, width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_container = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong = tk.PhotoImage(file="images/wrong.png")
btn_unknown = tk.Button(root, image=wrong, highlightthickness=0, command=next_card)
btn_unknown.grid(row=1, column=0)

right = tk.PhotoImage(file="images/right.png")
btn_known = tk.Button(root, image=right, highlightthickness=0, command=is_known)
btn_known.grid(row=1, column=1)

next_card()

root.mainloop()
