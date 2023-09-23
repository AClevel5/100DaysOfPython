# 1 Determine odd or even number
# number = int(input("Which number do you want to check? "))
# half = number % 2

# if half == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")

# 2 Conditional ticket prices.
# print("Welcome to the amusement park!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age >= 18:
#         print("Please pay $12.")
#     elif age <= 12:
#         print("Please pay $5.")
#     else:
#         print("Please pay $7")

# 3 Expanded BMI program. Will calculate BMI and tell you where you fall.
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# a = float(height)
# b = float(weight)
# c = a * a
# bmi = round(b / c)

# if bmi <= 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25.0:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30.0:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35.0:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")

# 4 Determine if it is a leap year.
# year = float(input("What is the year? "))

# four = year % 4
# one_hundred = year % 100
# four_hundred = year % 400

# if four == 0:
#     if one_hundred == 0:
#         if four_hundred == 0:
#             print("Leap")
#         else:
#             print("not leap")
#     else:
#         if four == 0:
#             print("Leap")
#         else:
#             print("Not Leap")
# else:
#     print("Not Leap")

# 5 Pizza program to calculate price.
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# price = 0

# # base sizes with Pep or not.
# if size == "L":
#     if add_pepperoni == "Y":
#         price = 28
#     else:
#         price = 25
# elif size == "M":
#     if add_pepperoni == "Y":
#         price = 23
#     else:
#         price = 20
# else:
#     if add_pepperoni == "Y":
#         price = 17
#     else:
#         price = 15

# if extra_cheese == "Y":
#     price += 1
# else:
#     "no change"

# print(f"Your final bill is: {price}")
