import math

h = int(input("What is the height of the walls? "))
w = int(input("what is the width of the walls? "))
c = 5

num_of_cans = (h * w) / c

round_num = math.ceil(num_of_cans)

print(f"You'll need {round_num} cans of paint")
