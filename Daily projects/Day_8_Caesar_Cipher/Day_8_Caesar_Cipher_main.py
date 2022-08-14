"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 8 - Caesar Cipher                                                                                 *
*    Subject: Function with inputs, positional and keyword arguments, function arguments                    *
*    Date: 2022-03-06                                                                                       *
*************************************************************************************************************
"""

# Day 8 project - Caesar Cipher

from Day_8_Caesar_Cipher.Day_8_art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1  # Reverse the shift amount to obtain the original word
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)  # This is the original position of the letter (h = 8)
            new_position = position + shift_amount  # new position after shifting
            end_text += alphabet[new_position]  # Add the alphabet at the new position to the end_text
        else:
            end_text += char  # characters not in the alphabet list above to remain un-shifted (numbers, space, symbols)
    print(f"Here's the {direction}d result: {end_text}")


wants_restart = True
while wants_restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26  # Using the remainder after dividing by 26 (the numbe of alphabets) will make sure that
    # entering a shift amount greater than 26 will still work

    # Now call the caesar to function
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    again = input("Do you want to restart? Type yes or no\n").lower()
    if again == "no":
        wants_restart = False
        print("Goodbye")
