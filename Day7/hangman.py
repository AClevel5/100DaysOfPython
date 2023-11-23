import random
from wordlist import word_list

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

random_word = random.choice(word_list)
display = []
word_length = len(random_word)
game_over = False
counter = 6

for _ in range(word_length):
    display += "_"

while game_over == False:
    chosen_letter = input("Choose a letter ").lower()

    for position in range(word_length):
        letter = random_word[position]
        if letter == chosen_letter:
            display[position] = letter
    if chosen_letter not in display:
        counter -= 1
    print(stages[counter])
    print(f"{' '.join(display)}")

    if "_" not in display:
        game_over = True
        print("WINNA")
    if counter == 0:
        game_over = True
        print("Loser")
