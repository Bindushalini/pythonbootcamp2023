from tkinter import *
import requests


def get_quote():
    resp = requests.get(url="https://api.kanye.rest")
    resp.raise_for_status()
    data = resp.json()
    canva.itemconfig(quote_text, text=data['quote'])


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canva = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canva.create_image(150, 207, image=background_img)
quote_text = canva.create_text(150, 207, text="", width=250, font=("Arial", 25, "bold"),
                               fill="white")
canva.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
