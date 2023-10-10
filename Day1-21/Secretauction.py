import os

print("Welcome to secret auction program")

my_dict = {}
input_val = "yes"
while input_val == "yes":
    os.system('cls')
    name = input("What is your name?")
    bid = input("What is your bid? Rs.")
    my_dict[name] = int(bid)
    input_val = input("Are there other bidders, type 'yes' or 'no'").lower()
val_list = []
for v in my_dict.values():
    val_list.append(v)
name = [i for i in my_dict if my_dict[i] == max(val_list)]
print(f"The winner is {name[0]} with a bid of Rs-{max(val_list)}")
