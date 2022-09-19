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


# TODO:  Exercise 26.3 - Data Overlap
"""
Instructions
Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are common in both files
"""
with open("file1.txt") as file1:
    file1_content = file1.readlines()
    file1_list = [int(n.strip("\n")) for n in file1_content]
with open("file2.txt") as file2:
    file2_content = file2.readlines()
    file2_list = [int(n.strip("\n")) for n in file2_content]
result = [n for n in file1_list if n in file2_list]
# Write your code above 👆

# print(file1_list)
# print(file2_list)
print(result)
