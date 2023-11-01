THEME_COLOR = "#375362"
from tkinter import *
from quizbrain import Quiz


class UserInterface:
    def __init__(self, quizmodule: Quiz):
        self.quiz = quizmodule
        self.window = Tk()
        self.window.title("Quiz game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score=0", font=("Arial", 10), fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canva = Canvas(width=300, height=250, bg="white", highlightthickness=0)

        self.question_text = self.canva.create_text(150, 125, text="Some question text", fill=THEME_COLOR
                                                    , font=("Arial", 20, "italic"), width=280)
        self.canva.grid(column=1, row=1, columnspan=2, pady=50)
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_img, bd=0, highlightthickness=0, command=self.check_correctness)
        self.false_button = Button(image=false_img, bd=0, highlightthickness=0, command=self.check_incorrectness)

        self.true_button.grid(column=1, row=2)
        self.false_button.grid(column=2, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canva.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score={self.quiz.user_score}")
            text = self.quiz.next_question()
            self.canva.itemconfig(self.question_text, text=text)
        else:
            self.canva.itemconfig(self.question_text, text="you have exhausted the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_correctness(self):
        self.update(self.quiz.check_answer("True"))

    def check_incorrectness(self):
        self.update(self.quiz.check_answer("False"))

    def update(self, is_right):
        if is_right:
            self.canva.config(bg="green")
        else:
            self.canva.config(bg="red")
        self.window.after(500, self.get_next_question)