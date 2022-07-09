"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 5 - Password Generator                                                                            *
*    Subject: Python Loops                                                                                  *
*    Date: 2022-02-21                                                                                       *
*************************************************************************************************************
"""

# Exercise 5.1 - Average Height
"""Instructions You are going to write a program that calculates the average student height from a List of heights. 
Important You should not use the sum() or len() functions in your answer. You should try to replicate their 
functionality using what you have learnt about for loops. """

# Write your code below this row 👇
# 🚨 Don't change the code below 👇
student_heights = input(
    "Input a list of student heights ").split()  # split() takes the inputted height and make a list out of it
# separated by space
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])  # change the input string to integer for calculation
# 🚨 Don't change the code above 👆

total_height = 0
for height in student_heights:
    total_height += height

total_num = 0
for length in student_heights:
    total_num += 1
average = total_height / total_num
print(round(average))
