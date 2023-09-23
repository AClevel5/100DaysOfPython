# Change type of variable to add them together.
two_digit_number = input("Type a two digit number: ")

a = two_digit_number[0]
b = two_digit_number[1]
c = int(a)
d = int(b)

print(c + d)

# BMI Calculator weight / height^2
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
a = float(height)
b = float(weight)
c = a * a
print(int(b / c))

# Calculate how many days weeks month you have left to live if you live to 90

years = input("What is your current age? ")
years_int = int(years)
years_diff = 90 - years_int
days = 365 * years_diff
months = 12 * years_diff
weeks = 52 * years_diff

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
