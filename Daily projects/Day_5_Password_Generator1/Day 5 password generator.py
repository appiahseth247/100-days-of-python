"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 5 - Password Generator                                                                            *
*    Subject: Python Loops                                                                                  *
*    Date: 2022-02-21                                                                                       *
*************************************************************************************************************
"""

# Day 5 - Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
ters = random.choices(letters, k=nr_letters)  # random.choices(variable_name, k = number of element you want) syntax
# can be used to generate more 1 random elements from a list
bols = random.choices(symbols, k=nr_symbols)
bers = random.choices(numbers, k=nr_numbers)
password_elements = ters + bols + bers  # + can be used to concatenate multiple list together
print(password_elements)  # a list as of now
password = ""
for elements in password_elements:
    password += elements
print(f"Here is your password: {password}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = ""  # initialize password as a string
for elements in password_elements:
    password += elements
    password = list(password)  # to reshuffle a string, it must be changed to a list first
    random.shuffle(password)  # reshuffle
    password = ''.join(password)  # ''.join() to concatenate the list to string again
print(f"Here is your password: {password}")
