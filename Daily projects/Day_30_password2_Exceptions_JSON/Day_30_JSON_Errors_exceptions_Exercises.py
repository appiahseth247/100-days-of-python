"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 30 - Improved Password Manager and NATO Phonetics                                                 *
*    Subject:  JSON and Handling Error Exceptions                                                           *
*    Date: 2022-05-17                                                                                       *
*************************************************************************************************************
"""

# Exercise 30.1 - Handling IndexError

"""
Instructions
- We've got some buggy code. Try running the code. The code will crash and give you an IndexError. 
- This is because we're looking through the list of fruits for an index that is out of range.
- Use what you've learnt about exception handling to prevent the program from crashing
- If the user enters something that is out of range just print a default output of "Fruit pie".

Original code below
fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")


make_pie(4)

"""
# Solution
fruits = ["Apple", "Pear", "Orange"]


# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)
