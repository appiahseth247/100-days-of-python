"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 3 - Treasure Island                                                                               *
*    Subject: conditional statements, logical operators, Code blocks and Scope                              *
*    Date: 2022-02-13                                                                                       *
*************************************************************************************************************
"""

# Exercise 3.1 Odd or Even number
# Instructions: Write a program that works out whether if a given number is an odd or even number.
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")