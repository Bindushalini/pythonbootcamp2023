print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
direction = input("select direction, Left or right? choose L or R").upper()
if direction == 'L':
    task = input("Do u want to swim or wait?, chose S or W").upper()
    if task == "W":
        door = input("Select the door to go ahead, Red/Blue/Yellow? Choose R/Y/B")
        door = door.upper()
        if door == 'R':
            print("Burned by fire, Game over")
        elif door == "B":
            print("Eaten by Beasts, Game over")
        elif door == "Y":
            print("You win!")
        else:
            print("Game Over")
    else:
        print("Attacked by trout.Game Over.")
else:
    print("Fall into a hole, Game over.")

