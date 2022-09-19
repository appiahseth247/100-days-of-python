"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 24 -  NATO Phonetic Alphabet                                                                      *
*    Subject:  List and Dictionary Comprehension                                                            *
*    Date: 2022-05-09                                                                                       *
*************************************************************************************************************
"""
import pandas

# TODO: Notes

"""
# Looping through a panda dataframe using dictionary comprehension


student_dict = {
    "students": ["Kofi", "Joyce", "Mike", "Ben"],
    "scores": [34, 43, 45, 66]
}

# Usual way for loping through a dict
# for (key, value) in student_dict.items():
# print(value)


student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
# loop through a dataframe just like a dict
# for (key, value) in student_data_frame.items():
#     print(key, value)

# using python in-built loop to loop through a row
for (index, row) in student_data_frame.iterrows():
    # print(row)
    # print(row.student) # to get hold of student name
    # print(row.score)  # to get hold of student score
    if row.students == "Kofi":
        print(row.scores)  # To print Kofi's score only
"""


# Day 26 project - NATO Phonetic Alphabet

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetics_dict = {row.letter: row.code for (index, row) in dataframe.iterrows()}
# print(nato_phonetics_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()

phonetic_words = [nato_phonetics_dict[letter] for letter in word]
print(phonetic_words)
