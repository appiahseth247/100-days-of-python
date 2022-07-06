"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 4 - Rock Paper Scissors                                                                           *
*    Subject: Randomisation and python list                                                                 *
*    Date: 2022-02-20                                                                                       *
*************************************************************************************************************
"""

# Exercise 4.2 - Banker Roulette (Who pays the bill)
"""Instructions You are going to write a program that will select a random name from a list of names. The person 
selected will have to pay for everybody's food bill. 

Important: You are not allowed to use the choice() function.

Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to 
work, you must enter all the names as names followed by comma then space. e.g. name, name, name 

When you run the code, just use a random number as the seed. e.g. 67346 It doesn't matter what you chose, 
it's only for our testing code to check your work. 

Example Input
Angela, Ben, Jenny, Michael, Chloe
Note: notice that there is a space between the comma and the next name.

Example Output
Michael is going to buy the meal today!
"""

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")  # split takes strings and put them into a list separated by whatever is in ("")
print(names)
lens = int(len(names) - 1)

# 🚨 Don't change the code above 👆

# Write your code below this line 👇
payer_number = random.randint(0, lens)
print(payer_number)
payer_name = names[payer_number]
print(f"{payer_name} is going to buy the meal today!")

# Using random.choice could have done the same thing too
"""payer_name = random.choice(names) #it picks an element directly from, the list
print(f"{payer_name} is going to buy the meal today!")"""
