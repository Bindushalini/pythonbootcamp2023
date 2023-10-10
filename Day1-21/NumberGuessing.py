import random
print("Today we will be building a number guessing game! Are u ready??!")
print("I have a number in mind between 1 and 100")
user_input = input("You have to guess the number! Choose your difficulty level : easy or hard: type 'e' or 'h'").lower()

HARD_LEVEL = 5
EASY_LEVEL = 10
random_number = random.randint(1, 100)
found_flag = False


def compare():
    global found_flag
    print(f"You have {user_input} attempts remaining to guess the correct number")
    user_number = int(input("Make a guess"))
    if user_number < random_number:
        format_string = "Too low\nGuess again"
    elif user_number > random_number:
        format_string = "Too high\n Guess again"
    else:
        format_string = f"You have guessed correctly. The answer is {random_number}"
        found_flag = True
    return format_string


if user_input == 'e':
    user_input = EASY_LEVEL
else:
    user_input = HARD_LEVEL
while user_input > 0 and not found_flag:
    print(compare())
    user_input -= 1

if not found_flag:
    print("You lose, no more guesses available ")