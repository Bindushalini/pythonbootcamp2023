import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print("We are in caesar cipher world!!")
print(f"{art.logo}")


def caesar(string_input, shift, direction):
    final_string = ""
    for letters in string_input:
        if letters.isalpha():
            str_index = alphabet.index(letters)
            if direction == "encode":
                final_string += alphabet[str_index + shift]
            else:
                final_string += alphabet[str_index - shift]
        else:
            final_string += letters
    print(f"The {direction}d text is:{final_string}")


ans = "yes"
while ans == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(text, shift, direction)
    ans = input("Type 'yes' to continue or 'no' to stop").lower()


