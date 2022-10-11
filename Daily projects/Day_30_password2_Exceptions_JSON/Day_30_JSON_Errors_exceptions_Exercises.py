"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 30 - Improved Password Manager and NATO Phonetics                                                 *
*    Subject:  JSON and Handling Error Exceptions                                                           *
*    Date: 2022-05-17                                                                                       *
*************************************************************************************************************
"""

# Exercise 30.3 - [Challenge] Handling KeywordError in Day 26 NATO phonetics
"""
Instructions
- For Day 26 main, if the user enters a number instead of a letter or word, the code will crash and report keyword Error
- Modify a part of the code and give feedback to the user to enter ONLY an alphabet in the English Language
- 
"""


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# Solution
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while KeyError:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Only English alphabet please")
    else:
        print(output_list)
        break

# ********* Angela's solution ********* but mine is better
# def generate_phonetic():
#     word = input("Enter a word: ").upper()
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#     except KeyError:
#         print("Only English alphabet please")
#         generate_phonetic()
#     else:
#         print(output_list)
#
#
# generate_phonetic()
