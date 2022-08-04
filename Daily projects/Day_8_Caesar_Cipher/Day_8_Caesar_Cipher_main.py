"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 8 - Caesar Cipher                                                                                 *
*    Subject: Function with inputs, positional and keyword arguments, function arguments                    *
*    Date: 2022-03-06                                                                                       *
*************************************************************************************************************
"""

# Exercise 8.2 - Prime Numbers Checker
"""
Instructions
You need to write a function that checks whether if the number passed into it is a prime number or not.
"""


def prime_checker():
    if n == 2 or n == 3 or n == 5 or n == 7:
        print("It's a prime number.")
    elif n % 3 == 0 or n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker()
