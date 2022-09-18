import random, pandas
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

# names = ["kofi", "Joyce", "Mike", "jkdsndfosl"]
# short_names = [name for name in names if len(name) == 4]
# long_names = [name.upper() for name in names if len(name) > 4]
"""

# TODO: Dictionary comprehension
# new_dict = {new_key:new_value for item in list}  : from a list
# new_dict = {new_key:new_value for (key:value) in dict.items() if test} : from a dict
# names = ["kofi", "Joyce", "Mike", "jkdsndfosl"]
# students_scores = {student: random.randint(1, 100) for student in names}
# print(students_scores)
# passed_students = {student: score for (student, score) in students_scores.items() if score > 60}
# print(passed_students)


# Exercise 26.1 - Dictionary comprehension (letters count)
"""
Instructions
Takes each word in the given sentence and calculates the number of letters in each word to make a dict
"""
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below
result = {word: len(word) for word in sentence.split()}  # .split() use words in a sentence to make a list of them
print(result)
