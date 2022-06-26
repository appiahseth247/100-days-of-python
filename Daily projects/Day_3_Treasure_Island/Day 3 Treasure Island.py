"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 3 - Treasure Island                                                                               *
*    Subject: conditional statements, logical operators, Code blocks and Scope                              *
*    Date: 2022-02-13                                                                                       *
*************************************************************************************************************
"""

# Exercise 3 - Leap Year

'''
Instructions:   Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.
'''
# To determine whether a year is a leap year, follow these steps:

# If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
# If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
# If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
# The year is a leap year (it has 366 days).
# The year is not a leap year (it has 365 days).

year = int(input("What year do you want to check? "))
if year % 4 ==0:
    if year % 100 ==0:
        if year % 400 ==0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")