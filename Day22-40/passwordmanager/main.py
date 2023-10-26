from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

GREEN = "#9bdeac"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    final_str_list = [choice(letters) for _ in range(nr_letters)] + [choice(symbols)
                                                                     for _ in range(nr_symbols)] + [
                         choice(numbers) for _ in range(nr_numbers)]
    shuffle(final_str_list)
    final_string = "".join(final_str_list)
    pyperclip.copy(final_string)
    pw_input.insert(0, final_string)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    if len(website_input.get()) == 0 or len(pw_input.get()) == 0:
        messagebox.showerror(title="invalid data", message="website or password input cannot be empty")
    else:
        is_ok = messagebox.askokcancel(title="confirm",
                                       message=f"are you sure about website: {website_input.get()}, username:{user_input.get()}")
        if is_ok:
            with open("my_data.txt", 'a') as fh:
                string_val = website_input.get() + " | " + user_input.get() + " | " + pw_input.get() + "\n"
                fh.write(string_val)
                website_input.delete(0, END)
                # user_input.delete(0, END)
                pw_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canva = Canvas(width=200, height=200, bg="white", highlightthickness=0)

ph = PhotoImage(file="logo.png")
canva.create_image(100, 100, image=ph)
# timer_text = canva.create_text(100, 130, text="00:00", fill="white", font=("white", 35, "bold"))

canva.grid(column=1, row=0)

website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

user_label = Label(text="Email/Username:", bg="white")
user_label.grid(column=0, row=2)

user_input = Entry(width=35)
user_input.grid(column=1, row=2, columnspan=2)
user_input.insert(0, "bindu23@gmail.com")

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

pw_input = Entry(width=21)
pw_input.grid(column=1, row=3)

gen_pw_button = Button(text="Gen password", bg="white", command=gen_pass)
gen_pw_button.grid(column=2, row=3)

add_button = Button(text="Add", bg="white", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
