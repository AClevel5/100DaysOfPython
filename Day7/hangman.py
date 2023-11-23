import random

word_list = ["aardvark", "baboon", "camel", "dog", "trout"]
random_word = random.choice(word_list)
print(random_word)
display = []
word_length = len(random_word)

for _ in range(word_length):
    display += "_"

chosen_letter = input("Choose a letter ").lower()
for position in range(word_length):
    letter = random_word[position]
    if letter == chosen_letter:
        display[position] = letter

print(display)
