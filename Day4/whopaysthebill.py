import random

names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
x = len(names)
y = random.randrange(0, x) - 1
z = names[y]
print(z + " is going to buy the meal today!")
