# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global  reps
    window.after_cancel(timer)
    text = "00:00"
    canva.itemconfig(timer_text, text=text)
    unit_label.config(text="Timer")
    check_mark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 2 != 0 and reps <= 8:
        unit_label.config(text="WORKING", fg=PINK, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
        countdown(work_sec)
    elif reps == 8:
        unit_label.config(text="BREAK", fg=RED, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
        countdown(long_break)

    elif reps % 2 == 0:
        unit_label.config(text="SHORT DISPERSE", fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
        countdown(short_break)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global reps
    min = math.floor(count / 60)
    sec = math.floor(count % 60)
    if sec < 10:
        sec = f"0{sec}"
    data_string = f"{min}:{sec}"

    canva.itemconfig(timer_text, text=data_string)
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start()
        mark_count = math.floor(reps/2)
        marks = ""
        for _ in range(mark_count):
            marks += "✔"
        check_mark.config(text=marks)


        # ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("POMODORA TIMER")
window.config(padx=100, pady=50, bg=YELLOW)

canva = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

ph = PhotoImage(file="tomato.png")
canva.create_image(100, 112, image=ph)
timer_text = canva.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canva.grid(column=1, row=1)

unit_label = Label(text="Timer", fg=GREEN, font=20, bg=YELLOW)
unit_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start)
start_button.grid(column=0, row=2)

res_button = Button(text="Reset", command=reset)
res_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW, font=13)
check_mark.grid(column=1, row=2)

window.mainloop()
