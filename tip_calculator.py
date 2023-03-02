print("\n")
print("Welcome to the tip calculator!")
print("\n")
bill = float(input("What was the total bill? $"))
print("\n")
tip = int(input("How much tip would you like to give? 15, 17, 20? "))
print("\n")
people = int(input("How many people to split the bill? "))
print("\n")

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")
print("\n")