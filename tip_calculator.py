# score=0
# height=1.8
# isWinning=True

# print(str(score) +" "+str(height))

print("Welcome to tip calculator")
total_bill = float(input("What is the total bill? "))
tip = int(input("What percentage of tip you would like to give 10 ,12 or 15? "))
people = int(input("How many people are splitting the bill?"))

tip_Percent = (tip / 100) * total_bill
new_total_bill = total_bill + tip_Percent
print(f"Each person should pay {round(new_total_bill/people,2)}")
