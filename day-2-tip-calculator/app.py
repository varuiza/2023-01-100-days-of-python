# If the bill was 150€, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Round the result to 2 decimal places.

print("\n------------------------------")
print("Welcome to the Tip Calculator!")
print("------------------------------\n")

bill = float(input("What was the total bill?\n"))
tip = int(input(
    "\nHow much tip would you like to give? A good amount would be about 10 to 15.\n"))
people = int(input("\nHow many people need to split the bill?\n"))

total_bill = bill * (1 + (tip / 100))
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print("\n------------------------------")
print(f"Each person should pay: {final_amount}€")
print("------------------------------")
