"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 30 - Improved Password Manager and NATO Phonetics                                                 *
*    Subject:  JSON and Handling Error Exceptions                                                           *
*    Date: 2022-05-17                                                                                       *
*************************************************************************************************************
"""

# Exception Handling

try:  # Try doing this: Something that might cause an exception or error
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:  # Do this if there was an exception
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:  # Can raise as many exceptions as possibles
    print(f"The key {error_message} does not exist.")
else:  # Do this if there were no exceptions
    content = file.read()
    print(content)
# finally:  # Finally do this no matter what happens
#     raise TypeError("This is an error that I made up.")


# BMI Example
"""
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
"""


# TODO. JSON Files
"""
JavaScript Object Notation (JSON) is like a nested dictionary with key:value pair data structure
json.write(filename) = write to file
json.load(filename) = read a file
json.update(filename) = to add to a file
"""