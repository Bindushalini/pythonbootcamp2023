# Step 1
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
import random
word_list = ["aardvark", "baboon", "camel"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
my_random_word = random.choice(word_list)
lives = 6
display = ['-' for i in range(len(my_random_word))]
print(f"Guess the letter {display}")
game_ends = False
while not game_ends:
    guess = input("Hi, please guess a letter to determine the word").lower()
    for i in range(len(my_random_word)):
        if my_random_word[i] == guess:
            display[i] = my_random_word[i]
    print(display)
    if guess not in my_random_word:
        lives -= 1
        if lives == 0:
            game_ends = True
        print("oh no, not the correct letter.")
        print(stages[lives])

    if not '-' in display:
        print("You win!")
        game_ends = True
if '-' in display and game_ends:
    print("you loose")



