"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 24 -  lesson study notes                                                                          *
*    Subject:  List and Dictionary Comprehension                                                            *
*    Date: 2022-05-09                                                                                       *
*************************************************************************************************************
"""
# Day 26 lesson note and Exercises

"""
# TODO: List comprehension
# old_list = [1, 2, 3, 4]
# new_list = [n + 2 for n in old_list]
# print(new_list)
#
# n = "Lol"
# l = [l for l in n]

# num = [n * 2 for n in range(1, 5)]

# names = ["kofi", "Joyce", "Mike", "Ben"]
# short_names = [name for name in names if len(name) == 4]
# long_names = [name.upper() for name in names if len(name) > 4]
"""

# TODO: Dictionary comprehension
# new_dict = {new_key:new_value for item in list}  : from a list
# new_dict = {new_key:new_value for (key:value) in dict.items() if test} : from a dict
# names = ["kofi", "Joyce", "Mike", "Ben"]
# students_scores = {student: random.randint(1, 100) for student in names}
# print(students_scores)
# passed_students = {student: score for (student, score) in students_scores.items() if score > 60}
# print(passed_students)


# TODO:  Exercise 26.4 - Squaring numbers (List comprehension)
"""
Instructions
You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain
 every number in the list numbers but each number should be squared.

"""
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

# Write your 1 line code 👇 below:
squared_numbers = [n ** 2 for n in numbers]

# Write your code 👆 above:

print(squared_numbers)
