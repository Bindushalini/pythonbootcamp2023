class Quiz:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.user_score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?")
        self.check_answer(user_answer, current_question)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_val, question):
        if user_val.lower() == question.answer.lower():
            self.user_score += 1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print(f"The correct answer is {question.answer}\nCurrent score is {self.user_score}/{self.question_number}\n")
