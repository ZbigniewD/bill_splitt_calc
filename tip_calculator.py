# Welcome to the tip calculator!
# What was the total bill? (input)
# How much tip would you like to give? (input) (percetn)
# How many people to split the bill? (input)
# Each person should pay: (output)

# Define variables
# I can change type while I declare a variable
total_bill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
number_of_people = int(input("How many people to split the bill?\n"))

# Computation: one_person_bill = (total_bill + tip) / number_of_people
# I have to make it as rounded float.
new_tip = (tip * total_bill) / 100 # percent
one_person_bill = (total_bill + new_tip) / number_of_people
rounded_bill = round(one_person_bill, 2)
rounded_bill = "{:.2f}".format(rounded_bill) #format 
# https://www.freecodecamp.org/news/python-string-format-python-s-print-format-example/

print(f"Each person should pay: ${rounded_bill}")

# Looks like I made mistake. Tip is a precetage.
