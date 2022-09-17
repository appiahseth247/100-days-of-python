"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 24 -  Working with Local Files and Directories                                                    *
*    Subject: Reading, writing and adding to a file                                                         *
*    Date: 2022-04-28                                                                                       *
*************************************************************************************************************
"""

# Day 24 Project 2 - Mail Merge project

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


"""
r = read only mode
w = write to a file. Deletes whatever is already in the file. If the file doesn't exist, the mode will create it
a = appends to what is already in the file
"""
with open("Input/Names/invited_names.txt", "r") as invited_names_file:
    invited_names_list = invited_names_file.readlines()  # Readlines() return content of a file as a list. splitlines()

with open("Input/Letters/starting_letter.txt", "r") as letter_file:
    starting_letter_content = letter_file.read()
    for name in invited_names_list:
        stripped_name = name.strip("\n")  # removes white spaces before and after a string or whatever is passed to it
        new_letter = starting_letter_content.replace("[name]", stripped_name)  # replace "[name]" in the starting
        # letter with the real names of those invited
        with open(f"./output/ReadyToSend/Letter_for_{stripped_name}", "w") as individual:  # a new file will be created
            individual.write(new_letter)  # and we write the new letter to it
