import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(alphabet)
# create a dictionary of data frame for all letters


new_dict = {names.letter: names.code for (_, names) in alphabet.iterrows()}
# for (_, names) in alphabet.iterrows():
#     new_dict.update({names.letter: names.code})
continue_input = True
while continue_input:
    user_name = input("Enter the name to get nato words").upper()
    try:
        output = [new_dict[value] for value in user_name]
    except KeyError as k:
        print("sorry input should always contain alphabets")
    else:
        print(output)
        continue_input = False
