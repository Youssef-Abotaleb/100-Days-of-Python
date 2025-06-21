#Tip Calculator

print("Welcome to the tip calculator ! ")
bill = input("What was the total bill ? ")
tip = input("how much tip would you like to give ? 10, 12, or 15 ? ")
split = input("how many people will split the bill ?")
calc = float(bill) + (float(bill)*(float(tip)/100))
total = calc/int(split)
print(f"Each person should pay: {round(total,2)}")