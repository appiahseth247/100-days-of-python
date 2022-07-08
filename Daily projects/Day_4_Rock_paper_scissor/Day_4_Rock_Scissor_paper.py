"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 4 - Rock Paper Scissors                                                                           *
*    Subject: Randomisation and python list                                                                 *
*    Date: 2022-02-20                                                                                       *
*************************************************************************************************************
"""

# Exercise 4.3 - Treasure Map
"""
Instructions
You are going to write a program that will mark a spot with an X.

In the starting code, you will find a variable called map.

This map contains a nested list. When map is printed this is what the nested list looks like:

['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']

In the starting code, we have used new lines (\n) to format the three rows into a square, like this:

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

This is to try and simulate the coordinates on a real map.

First, your program must take the user input and convert it to a usable format.

Next, you need to use it to update your nested list with an "x".

Example Input 1
column 2, row 3 would be entered as:

23
Example Output 1
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', 'X', '⬜️']
Example Input 2
column 3, row 1 would be entered as:

31
Example Output 2
['⬜️', '⬜️', 'X']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
"""
# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Enter the row and column number together (tow-digits): ")
# 🚨 Don't change the code above 👆

real_map = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

horizontal = int(position[0])  # the first digit entered has position 0, and it goes to select the particular list
# (to be worked on) among the entire list (real_map)

vertical = int(position[1])  # the 2nd digits locates the exact element
# (to be changed) among the elements in the selected list

selected_row = map[horizontal - 1][vertical - 1] = "X"  # the entered row and column are reduced by 1 because

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
