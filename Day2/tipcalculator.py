print("Welcome to the tip calculator! ")
tb = input("What was the total bill? ")
tip_percent = input("What percentage tip would you like to give? 10, 15, or 20? ")
people = input("How many people to split the bill? ")

tb_flt = float(tb)
tip_percent_flt = float(tip_percent)
percentage = tip_percent_flt / 100
percentage += 1
people_flt = float(people)

a = tb_flt * percentage
b = round(a / people_flt, 2)

print(f"Each person should pay: {b}")
