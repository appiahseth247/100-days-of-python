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


# TODO:  Exercise 26.5 - From degrees to Fahrenheit (Dictionary comprehension)
"""
Instructions
You are going to use Dictionary Comprehension to create a dictionary called `weather_f` that takes each temperature
 in degrees Celsius and converts it into degrees Fahrenheit.
"""
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆
# Write your code 👇 below:
weather_f = {day: temp_c * 9 / 5 + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)
