import html
class Quiz:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.user_score = 0
        self.current_question = ""

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"{self.question_number}: {q_text}"
        # user_answer = input(f"Q.{self.question_number}: {q_text}. (True/False)?")
        # self.check_answer(user_answer, current_question)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_val):
        if user_val.lower() == self.current_question.answer.lower():
            self.user_score += 1
            return True
        return False
        # print(f"The correct answer is {question.answer}\nCurrent score is {self.user_score}/{self.question_number}\n")
