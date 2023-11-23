import random

word_list = ["aardvark", "baboon", "camel", "dog", "trout"]
random_word = random.choice(word_list)
print(random_word)
chosen_letter = input("Choose a letter ").lower()
display = []

for x in random_word:
    display.append("_")

for letter in random_word:
    if letter == chosen_letter:
        print("Right")
    else:
        print("Wrong")
