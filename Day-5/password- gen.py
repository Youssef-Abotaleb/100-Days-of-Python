import random

letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
symbols = list('!#$%&()*+')

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

if nr_letters > len(letters):
    print(f"Too many letters requested! Max allowed is {len(letters)}.")
    exit()
if nr_symbols > len(symbols):
    print(f"Too many symbols requested! Max allowed is {len(symbols)}.")
    exit()
if nr_numbers > len(numbers):
    print(f"Too many numbers requested! Max allowed is {len(numbers)}.")
    exit()

password = []
password += random.sample(letters, nr_letters)
password += random.sample(symbols, nr_symbols)
password += random.sample(numbers, nr_numbers)

random.shuffle(password)

fpass = ''.join(password)
print(fpass)
