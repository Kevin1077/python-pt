print("Welcome to the tip calculator")

bill=input("What was the total bill?\n")


tip=input("what is percentage of tip would you like to give? 10, 12, or 15?\n ")

people=input("how many people to split the bill\n")

bill=int(bill)
tip=int(tip)
people=int(people)

payment=round((bill+(bill*tip/100))/people,2)
print(f"Each person should pay: ${payment}")