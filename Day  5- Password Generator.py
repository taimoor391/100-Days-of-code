#Create a password generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#for i in range(0,nr_letters):
random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)
let=""
num=""
symb=""
for i in range(0,nr_numbers):
   let=let+letters[i]
for j in range(0, nr_symbols):
       num =num +symbols[j]
for z in range(0, nr_numbers):
           symb =symb +numbers[z]
initipass=(let+num+symb)
pass1=list(initipass)
random.shuffle(pass1)
password="".join(pass1)
print(len(password))

