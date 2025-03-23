# question_data = [
#     {"text": "A slug's blood is green.", "answer": "True"},
#     {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#     {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
#     {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
#     {
#         "text": "In West Virginia, USA, if you accidentally hit an animal with your car,
#         you are free to take it home to eat.",
#         "answer": "True"},
#     {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
#      "answer": "False"},
#     {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#     {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
#     {"text": "Google was originally called 'Backrub'.", "answer": "True"},
#     {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
#     {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
#     {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]

# question_data = [
#         {
#             "category": "General Knowledge",
#             "type": "boolean",
#             "difficulty": "easy",
#             "question": "Video streaming website YouTube was purchased in it&#039;s "
#                         "entirety by Facebook for US$1.65 billion in stock.",
#             "correct_answer": "False",
#             "incorrect_answers": [
#                 "True"
#             ]
#         },
#         {
#             "category": "General Knowledge",
#             "type": "boolean",
#             "difficulty": "easy",
#             "question": "It is automatically considered entrapment in the United States if the police "
#                         "sell you illegal substances without revealing themselves.",
#             "correct_answer": "False",
#             "incorrect_answers": [
#                 "True"
#             ]
#         },
#         {
#             "category": "General Knowledge",
#             "type": "boolean",
#             "difficulty": "easy",
#             "question": "Bulls are attracted to the color red.",
#             "correct_answer": "False",
#             "incorrect_answers": [
#                 "True"
#             ]
#         },
#         {
#             "category": "General Knowledge",
#             "type": "boolean",
#             "difficulty": "easy",
#             "question": "&quot;Ananas&quot; is mostly used as the word for Pineapple in other languages.",
#             "correct_answer": "True",
#             "incorrect_answers": [
#                 "False"
#             ]
#         },
#         {
#             "category": "General Knowledge",
#             "type": "boolean",
#             "difficulty": "easy",
#             "question": "The Sun rises from the North.",
#             "correct_answer": "False",
#             "incorrect_answers": [
#                 "True"
#             ]
#         },
#         {
#             "category": "General Knowledge",
#             "type": "boolean",
#             "difficulty": "easy",
#             "question": "You can legally drink alcohol while driving in Mississippi.",
#             "correct_answer": "True",
#             "incorrect_answers": [
#                 "False"
#             ]
#         },
#         {
#             "category": "General Knowledge",
#             "type": "boolean",
#             "difficulty": "easy",
#             "question": "In 2010, Twitter and the United States Library of Congress partnered "
#                         "together to archive every tweet by American citizens.",
#             "correct_answer": "True",
#             "incorrect_answers": [
#                 "False"
#             ]
#         },
#         {
#             "category": "General Knowledge",
#             "type": "boolean",
#             "difficulty": "easy",
#             "question": "Slovakia is a member of European Union-",
#             "correct_answer": "True",
#             "incorrect_answers": [
#                 "False"
#             ]
#         },
#         {
#             "category": "General Knowledge",
#             "type": "boolean",
#             "difficulty": "easy",
#             "question": "The mitochondria is the powerhouse of the cell.",
#             "correct_answer": "True",
#             "incorrect_answers": [
#                 "False"
#             ]
#         },
#         {
#             "category": "General Knowledge",
#             "type": "boolean",
#             "difficulty": "easy",
#             "question": "Jingle Bells was originally meant for Thanksgiving",
#             "correct_answer": "True",
#             "incorrect_answers": [
#                 "False"
#             ]
#         }
#     ]
import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}
data_response = requests.get(url="https://opentdb.com/api.php", params=parameters)
data_response.raise_for_status()
question_data = data_response.json()['results']
