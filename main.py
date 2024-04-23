import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def cipher(choice, word, shift_amount):
    end_text = ""

    if choice == "decode":
        shift_amount *= -1

    for char in word:
        if char in alphabet:
            pos = alphabet.index(char)
            new_pos = (pos + shift_amount) % 26
            end_text += alphabet[new_pos]
        else:
            end_text += char
    print(f"The {choice}d text is {end_text}")


should_continue = True
while should_continue == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    cipher(direction, text, shift)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if result == "no":
        should_continue = False
        print("Goodbye!")