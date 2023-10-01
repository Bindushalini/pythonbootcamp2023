# Day 4
# import random
#
# random_integer = random.randint(1, 10)
# print(random_integer)
#
# random_float = random.random()# generates between 0 and 1
# print(random_float)

# lists
# dirty_dozen = ["strawberries", "Necta" ]
# vege = ["potato", "tomato"]
# two_list = [dirty_dozen, vege]
# print(two_list)

# Day 5
# fruits = ["apple", "pear", "watermelon"]
# for f in fruits:
#     print(f)

# day6
# def abc():
#     print("world")
# abc()
# day 8:
# def greet(name):
#     print("I am inside greet function, hi "+name)
#     print("Second line")
#     print("ending")
#
#
# greet("poser")
#
#
# def greet(name, location):
#     print(f"inside new function of greet with arguments: name {name}, at location {location}")
#
#
# greet(name="Bindu", location="Bangalore")

# Day 9:
# dictionaries
# my_dict = {0: "Monday", 1: "Tuesday", 2: "Wednesday"}
# print(my_dict[1])
# my_dict[5] = "Friday"
# print(my_dict)
#
# for x in my_dict:
#     print(my_dict[x])
#
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
#
# student_grades = {}
#
#
# def get_grades(score):
#     grade = ""
#     if 91 <= score <= 100:
#         grade = "Outstanding"
#     elif 81 <= score <= 90:
#         grade = "Exceeds Expectations"
#     elif 71 <= score <= 80:
#         grade = "Acceptable"
#     elif score <= 70:
#         grade = "Fail"
#     else:
#         pass
#     return grade
#
#
# for value in student_scores:
#     student_grades[value] = get_grades(student_scores[value])
#
# print(student_grades)
#
# state = {
#     "Karnataka": ["rice", "Bangalore", "Kannada"],
#     "Maharashtra": ["Jowar", "Mumbai", "Marathi"],
#     "Kerala": {"Main_crops": ["Coconuts", "Tea", "Cloves"], "captial": "Thiruvananthapuram",
#                "local_language": "Malayalam"}
# }
# print(state)
# print(state["Kerala"]["Main_crops"])
#
# Education = [
#     {"Baby": "basic of languages", "age_group": "1-5"},
#     {"Preschooler": "Letters, numbers, games", "age_group": "5-7"}
# ]
# print(Education[1]["age_group"])

# Day 10:

# def format_name(first_name, last_name):
#     if first_name == "" or last_name == "":
#         return "Emptystrin", "EmptyString"
#     first_name = first_name.title()
#     last_name = last_name.title()
#     return first_name, last_name
#
#
# update_f_name, update_l_name = format_name("bindu", "viGnesh")
# update_f_name, update_l_name = format_name("", "x")
#
# print(update_f_name, update_l_name)
