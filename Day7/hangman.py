import random

word_list = ["aardvark", "baboon", "camel", "dog", "trout"]
random_word = random.choice(word_list)
print(random_word)
display = []
word_length = len(random_word)
game_over = False
counter = 0

for _ in range(word_length):
    display += "_"

while game_over == False:
    chosen_letter = input("Choose a letter ").lower()
    counter += 1
    for position in range(word_length):
        letter = random_word[position]
        if letter == chosen_letter:
            display[position] = letter
            print(display)
    if "_" not in display:
        game_over = True
        print("WINNA")
    if counter == 6:
        game_over = True
        print("Loser")
