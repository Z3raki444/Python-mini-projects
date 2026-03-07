print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split_people = int(input("How many people to split the bill? "))
tip_amount = (tip_percentage / 100) * total_bill
total_amount = total_bill + tip_amount
amount_per_person = total_amount / split_people
print(f"Total bill: ${total_bill:.2f}")
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total amount to pay: ${total_amount:.2f}")
print(f"Amount per person: ${amount_per_person:.2f}")