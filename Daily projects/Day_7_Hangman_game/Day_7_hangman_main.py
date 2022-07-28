"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 6 - Hangman Game                                                                                  *
*    Subject: Application of Functions, Loops, If/Else Statements, range                                    *
*    Date: 2022-03-03                                                                                       *
*************************************************************************************************************
"""

import random
from Day_7_hangman_art import stages, logo
from Day_7_hangman_words import word_list, days, months_days, sentences
import os

# If you're using PyCharm, you need to enable the "Emulate Terminal in Console" toggle before any coding will work.
# Go to Run, Edit Configurations, and Execution. Then you can use the import os, os.system("clear")

username = input("What's your name?: ")
print(f"Hey {username}!, Welcome to the hangman game!\nYour goal is guess the corrct word")
print(logo)

# TODO-6: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6
lives = 6

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(months_days)

# TODO-2: - Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'. So if
#  the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to
#  guess.
display = []
for letter in range(len(chosen_word)):
    display += "_"
print(display)

# TODO-5: Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the
#  letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
# "_" in display: This also works instead of using the flag end_of_game
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ")
    # Use the clear() function imported from replit to clear the output between guesses.
    # clear()  # for pycharm
    os.system('cls')
    if guess in display:
        print(f"You've already guessed {guess}")

    # TODO-3: - Loop through each position in the chosen_word;
    #  If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    #  e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for position in range(len(chosen_word)):  # range(5) for apple
        if chosen_word[position] == guess:  # apple[1] = p
            display[position] = guess  # ["_", "p", "p", "_", "_"]

    # TODO-7: - If guess is not a letter in the chosen_word,Then reduce 'lives' by 1.
    #  If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}', which is not in the word. So, you lose a precious life:(")
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word is : {chosen_word}")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # TODO-4: - Print 'display' and you should see the guessed letter in the correct position and every other letter
    #  replace with "_". Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in
    #  TODO-5.

    if "_" not in display:
        end_of_game = True
        print("You win")
        print(f"The word is indeed : {chosen_word}")

    # TODO-8: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has
    #  remaining.
    print(stages[lives])
