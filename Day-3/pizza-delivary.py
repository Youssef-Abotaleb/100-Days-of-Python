print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want ? S, M or L : ")
pepperoni = input("Do you want pepperoni on your pizza ? Y or N : ")
extra_cheese = input("Do you want extra cheese ? Y or N : ")

bill = 0
if size == 'S' :
    bill += 15
elif size == 'M':
    bill += 20
else : 
    bill +=25

if pepperoni == 'Y' :
    bill += 2

if extra_cheese == 'Y':
    bill +=2

print(f"The total bill is {bill}")