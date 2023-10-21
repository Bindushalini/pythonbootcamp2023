#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

input_path = "./Input/Letters/starting_letter.txt"
input_names = "./Input/Names/invited_names.txt"
output_path = "./Output/ReadyToSend/"
letter_data = []
with open(input_path, 'r') as fh:
    letter_data = fh.readlines()


with open(input_names, 'r') as fh:
    data = fh.read().splitlines()
    for names in data:
        new_data = list(letter_data)
        new_data[0] = new_data[0].replace("[name]", names)
        string_data = "".join(new_data)
        file_name = "letter_to_"+names+".txt"
        with open(output_path+"/"+file_name, 'w') as write_handle:
            write_handle.write(string_data)
