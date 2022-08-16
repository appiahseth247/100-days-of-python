"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 12 - Number Guessing Game                                                                         *
*    Subject: Namespace: Local scope, global scope and python constants                                     *
*    Date: 2022-03-18                                                                                       *
*************************************************************************************************************
"""
# Day 12 project - Number Guessing game

"""Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode)."""

import random
from Day_12_art import logo

TURN_FOR_EASY = 10
TURN_FOR_HARD = 5


def guessing_game():
    print(logo)
    print('''Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100. Can you guess it?  \n''')
    attempt_left = 0  # just set up this variable
    select_level = input("Choose a difficulty. Type 'easy' or 'hard': easy: ")
    if select_level == "easy":
        attempt_left = TURN_FOR_EASY
        print("You have 10 attempts remaining to guess the number.\n")
    elif select_level == "hard":
        attempt_left = TURN_FOR_HARD
        print("You have 5 attempts remaining to guess the number.\n")
    computer_choice = random.randint(0, 100)
    # print(f"Pssst, the correct answer is {computer_choice}")

    number_not_guessed = True
    while number_not_guessed:
        user_choice = int(input("Please guess a number between 0 and 100: \n"))
        if computer_choice == user_choice:
            number_not_guessed = False
            print(f"You got it! The answer was {computer_choice}\n")
        else:
            attempt_left -= 1
            if user_choice > computer_choice:
                print(
                    f"That is too high!\nGuess again.\n\nYou have {attempt_left} attempts remaining to guess the "
                    f"number.\n")
            else:
                print(
                    f"That is too low!\nGuess again.\n\nYou have {attempt_left} attempts remaining to guess the "
                    f"number.\n")
            if attempt_left == 0:
                number_not_guessed = False
                print("You've run out of guesses, you lose.")
                print(f"Pssst, the correct answer is {computer_choice}")


guessing_game()
