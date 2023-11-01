from question_model import Question
from data import question_data
from quizbrain import Quiz
from ui import UserInterface
question_bank = []
for data in question_data:
    question_bank.append(Question(data['question'], data['correct_answer']))

quiz = Quiz(question_bank)
ui = UserInterface(quiz)
# while quiz.still_has_questions():
#     quiz.next_question()
print(f"You have completed the quiz\nYour final score is {quiz.user_score}/{quiz.question_number}\n")


