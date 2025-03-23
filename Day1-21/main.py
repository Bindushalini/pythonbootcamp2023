# Day 1
# basics of python
print('Hello world!!')
print("Hello world!\nHello world!\nYikes")
print('Hello Bindu shalini ' + ' ' + 'how is ur day?')
# input("Would you like some tea?")
x = 12
y = 13
tmp = x
x = y
y = tmp

print(x, y)
x = "FPGA_0A"
y = x.lstrip("FPGA_")
print(y)

# Day 2:
print("hello"[4])

print(123+345)
print(123_56)

# float
print(3.1416)
# boolen - true / false

# x = len(input("name please?"))
# print(type(x))
# print(" your name has " + str(x) + " chars")

score = 1
score1 = 1.0
print(f"score is {score}, {score1}")

# day 3:
# conditionals
x = 30
if x > 30:
    print("value greater")
else:
    print("lesser")

# leap year
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if (year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
        print("Leap year.")
    else:
        print("Not leap year.")
else:
    print("Not leap year.")
# love calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()
final_string = name1+name2
true_count = final_string.count('t')+final_string.count('r')+final_string.count('u')+final_string.count('e')
love_count = final_string.count('l')+final_string.count('o')+final_string.count('v')+final_string.count('e')
final_count = int(str(true_count)+str(love_count))
if final_count < 10 or final_count > 90:
    print(f"Your score is {final_count}, you go together like coke and mentos.")
elif 40 < final_count < 50:
    print(f"Your score is {final_count}, you are alright together.")
else:
    print(f"Your score is {final_count}.")