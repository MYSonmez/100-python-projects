import art

logo = art.logo

print(logo)

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""

    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            shift_amount = int(shift_amount % 26)
            if cipher_direction.lower() == "encode":
                new_position = position + shift_amount
            elif cipher_direction.lower() == "decode":
                new_position = position - shift_amount

            new_letter = alphabet[new_position]
            end_text += new_letter
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}\n")


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

again = input("Type 'yes' if you want to go again. Otherwise type 'no':\n")

while again.lower() == "yes":
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    again = input("Type 'yes' if you want to go again. Otherwise type 'no':\n")

if again.lower() == "no":
    print("\nGoodbye :)")
