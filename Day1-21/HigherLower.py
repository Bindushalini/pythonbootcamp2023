import data
import random

# get the random data from data - A and B
# ask the user to guess who has more followers.
# based on user input, retrieve the followers number and compare.
# if its right, add to score, compare previous B person with new A person
# if wrong , show message and end the program.

print("We are playing higher lower game")
keep_playing = True
randomA_person = random.choice(data.data)
score = 0


def get_result(A, B, user_choice):
    res = ""
    if (A > B and user_choice == 'A') or (A < B and user_choice == 'B'):
        res = "Wins"
    elif (A < B and user_choice == 'A') or (A > B and user_choice == 'B'):
        res = "Loose"
    return res


while keep_playing:
    print(f"Compare A: {randomA_person['name']}, a {randomA_person['description']}, from {randomA_person['country']}.")
    randomB_person = random.choice(data.data)
    while randomA_person == randomB_person:
        randomB_person = random.choice(data.data)
    print("VS".upper())
    print(f"Compare B: {randomB_person['name']}, a {randomB_person['description']}, from {randomB_person['country']}.")
    user_choice = input("Who has more followers? Type 'A' or 'B'?")
    output = get_result(randomA_person['follower_count'], randomB_person['follower_count'], user_choice)
    if output == "Loose":
        print(f"sorry you loose, you final score is {score}")
        keep_playing = False
    else:
        score += 1
        print(f"you are right, Current score{score}")
        randomA_person = randomB_person
