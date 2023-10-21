# Day 22

# pin pong game
# 1. 2 players moving at the side of screen
# 2. midline
# 3. ball moving diagonally across the screen
# 4. bounce back
# 5. detect collision
# 6. update score, reduce / increase the score
#
#
#  Day 23: Turtle capstone project

# 1. create a turtle and navigate it using up keypress.
# 2. create a car manager to create cars at required position, size, and move
# 3. detect collision and level up conditions
# 4. display the score / game over sequence

# Day24:
# updates to snake game
# files
# customising names in same files to multiple people

# with open("my_text.txt") as fh:
#     stri = fh.read()
#     print(stri)
with open("my_text.txt", "a") as fh:
    new_text = "adding text"
    fh.write(new_text)
