from tkinter import *


def calculate():
    miles = my_input.get()
    km = 1.609 * float(miles)
    kilo_label.config(text=km)


window = Tk()
window.title("Convertor from miles to km")
window.config(padx=150, pady=150)
window.minsize(width=300, height= 200)
my_input = Entry(width=7)

my_input.grid(column=0, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=1, row=0)

is_equal_label = Label(text="=")
is_equal_label.grid(column=0, row=1)

kilo_label = Label(text="0")
kilo_label.grid(column=1, row=1)

unit_label = Label(text="km")
unit_label.grid(column=2, row=1)

res_button = Button(text="Calculate", command=calculate)
res_button.grid(column=1, row=5)

window.mainloop()
