# Password Generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator")

nr_letters = int(input("How many letters would you like in your password ? : "))
nr_numbers = int(input("How many numbers would you like in your password ? : "))
nr_symbols = int(input("How many symbols would you like in your password ? : "))

print("\n")

password = ""

for i in range(1, nr_letters+1):
    password += random.choice(letters)

for j in range(1, nr_numbers+1):
    password += random.choice(numbers)

for k in range(1, nr_symbols+1):
    password += random.choice(symbols)

print(f"The easy password is : {password}")

strong_password = []

for i in range(1, nr_letters+1):
    strong_password.append(random.choice(letters))

for j in range(1, nr_numbers+1):
    strong_password.append(random.choice(numbers))

for k in range(1, nr_symbols+1):
    strong_password.append(random.choice(symbols))

random.shuffle(strong_password)

new_password = ""

for i in strong_password:
    new_password += i

print(f"The strong password is : {new_password}")