import random

word_list = ["aardvark", "baboon", "camel", "dog", "trout"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_word = random.choice(word_list)
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
chosen_letter = input("Choose a letter ").lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
