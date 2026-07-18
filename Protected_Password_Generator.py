import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#easy level
pwd=""
for i in range(nr_letters):
    pwd+=random.choice(letters)
for i in range (nr_symbols):
    pwd+=random.choice(symbols)
for i in range(nr_numbers):
    pwd+=random.choice(numbers)

print(pwd)

#hard level

pwd_list=[]
for i in range(nr_symbols):
    pwd_list.append(random.choice(symbols))
for i in range(nr_letters):
    pwd_list.append(random.choice(letters))
for i in range(nr_numbers):
    pwd_list.append(random.choice(numbers))
pwd1=""
print(pwd_list)
random.shuffle(pwd_list)
print(pwd_list)

for i in pwd_list:
    pwd1+=i

print(pwd1)

