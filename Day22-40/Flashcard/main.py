import os
import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"
WORD_FONT = ("Ariel", 50, "bold")
LANG_FONT = ("Ariel", 40, "italic")

if os.path.isfile("data/words_to_learn.csv"):
    my_df = pandas.read_csv("data/words_to_learn.csv", names=['French', 'English'], header=0)
    # to replace existing header names with names, pass names and header option
else:
    my_df = pandas.read_csv("data/french_words.csv")

my_df_dict = {lang.French: lang.English for (_, lang) in my_df.iterrows()}
random_french_word = ""


# ------------------FLIP OPERATION-------------------
def flip_card():
    global random_french_word
    canva.itemconfig(language, text="English", fill="white")
    canva.itemconfig(lang_word, text=my_df_dict[random_french_word], fill="white")
    canva.itemconfig(card_image, image=bh)


#  ------------------BUTTON OPERATIONS ------------------
def check_correctness():
    global random_french_word, flip_timer
    window.after_cancel(flip_timer)
    random_french_word = random.choice(list(my_df_dict.keys()))
    canva.itemconfig(language, text="French", fill="black")
    canva.itemconfig(lang_word, text=random_french_word, fill="black")
    canva.itemconfig(card_image, image=ph)
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    global random_french_word
    my_df_dict.pop(random_french_word, "")
    # print(len(my_df_dict))
    # print(my_df_dict)
    new_df = pandas.DataFrame.from_dict(my_df_dict, orient="index")
    new_df.to_csv("data/words_to_learn.csv")
    check_correctness()

#  --------------------UI -----------------


window = Tk()

window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
canva = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

ph = PhotoImage(file="images/card_front.png")
bh = PhotoImage(file="images/card_back.png")
card_image = canva.create_image(400, 263, image=ph)

canva.grid(row=0, column=0, columnspan=2)

language = canva.create_text(400, 150, text="Title", font=LANG_FONT)
lang_word = canva.create_text(400, 263, text="Word", font=WORD_FONT)

image1 = PhotoImage(file="images/right.png")
correct_button = Button(image=image1, highlightthickness=0, bd=0, command=is_known)
correct_button.grid(row=1, column=1)

image2 = PhotoImage(file="images/wrong.png")
incorrect_button = Button(image=image2, highlightthickness=0, bd=0, command=check_correctness)
incorrect_button.grid(row=1, column=0)
check_correctness()

window.mainloop()
