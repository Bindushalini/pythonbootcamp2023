import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇


name_list = ["rock", "paper", "scissor"]
rps_list = [rock, paper, scissors]
user_choice = int(input("Hi Gamer, what is your choice? Rock / paper/ scissors? Choose 0/1/2 respectively"))
print(name_list[user_choice], "\n", rps_list[user_choice])
computer_choice = random.randint(0, 2)


comp_win = "Computer Wins"
user_win = "User wins"
draw_str = "Its a draw"
final_msg = ""
if user_choice == computer_choice:
    final_msg = draw_str
elif user_choice == 0:
    if computer_choice == 1:
        final_msg = comp_win
    else:
        final_msg = user_win
elif user_choice == 1:
    if computer_choice == 0:
        final_msg = user_win
    else:
        final_msg = comp_win
else:
    if computer_choice == 0:
        final_msg = comp_win
    else:
        final_msg = user_win
print("Computers choice is:")
print(name_list[computer_choice], "\n", rps_list[computer_choice])
print(final_msg)
