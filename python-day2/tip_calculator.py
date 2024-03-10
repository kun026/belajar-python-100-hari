print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip You like to give? 10, 12, or 15? "))
people = int(input("How many people to the split the bill? "))

total_tip = tip / 100 * bill
# bill_with_tip = round((bill + total_tip) / people, 2)
bill_with_tip = "{:.2f}".format((bill + total_tip) / people)
print(f"Each person should pay: ${bill_with_tip}")


