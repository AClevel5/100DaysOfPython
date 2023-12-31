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

direction = input("Type 'encrypt' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position > 25:
            new_position = new_position - 26
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(cipher_text)


def decode(plain_text, shift_amount):
    decipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        if new_position < 0:
            new_position = new_position + 26
        new_letter = alphabet[new_position]
        decipher_text += new_letter
    print(decipher_text)


if direction == "encrypt":
    encrypt(text, shift)
elif direction == "decode":
    decode(text, shift)
