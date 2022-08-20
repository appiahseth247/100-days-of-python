"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 14 - Higher or Lower Game                                                                         *
*    Subject: Tips for Debugging a code                                                                     *
*    Date: 2022-03-20                                                                                       *
*************************************************************************************************************
"""
# Day 14 Project - Higher Lower Game

import os
import random
from Day_14_data import data
from Day_14_art import logo, vs

# TODO 1: select two people randomly from the data
first_person = random.choice(data)
second_person = random.choice(data)
while first_person == second_person:
    second_person = random.choice(data)

# TODO 2: assign the follower count of each person to a variable
first_person_followers = int(first_person["follower_count"])
second_person_followers = int(second_person["follower_count"])

print(logo)
print(f"Compare A: {first_person['name']}, a {first_person['description']}, from {first_person['country']}")
print(vs)
print(f"Against B: {second_person['name']}, a {second_person['description']}, from {second_person['country']}")

score = 0
ans_correct = True
while ans_correct:
    user_choice = input("Who has more followers on Instagram? Type 'A' or 'B': ").upper()
    if first_person_followers >= second_person_followers:
        if user_choice == 'A':  # which is correct answer
            score += 1  # increase score by 1
            os.system('cls')
            print(f"You're right! Current score: {score}")  # Give feedback and score
            first_person = second_person  # Now the data of the second person is shifted to that of the first person
            first_person_followers = second_person["follower_count"]  # Hence, second person followers is giving to 1st
            second_person = random.choice(data)  # Now choose a new second person from the data
            while first_person == second_person:
                second_person = random.choice(data)  # keeping choose until a person different from the 1st is chosen
            second_person_followers = second_person['follower_count']

            print(logo)

            print(f"Compare A: {first_person['name']}, a {first_person['description']}, from {first_person['country']}")

            print(vs)
            print(f"Against B: {second_person['name']}, a {second_person['description']}, "
                  f"from {second_person['country']}")
        else:
            ans_correct = False
            print(f"\nSorry, that's wrong.\n\n{first_person['name']} has {first_person_followers} followers\n"
                  f"{second_person['name']} has {second_person_followers} followers\n\nFinal score: {score}")

    if second_person_followers > first_person_followers:
        if user_choice == 'B':
            score += 1
            os.system('cls')
            print(f"You're right! Current score: {score}")
            first_person = second_person
            first_person_followers = second_person["follower_count"]
            second_person = random.choice(data)
            while first_person == second_person:
                second_person = random.choice(data)
            second_person_followers = second_person['follower_count']
            print(logo)
            print(f"Compare A: {first_person['name']}, a {first_person['description']}, from {first_person['country']}")
            print(vs)
            print(f"Against B: {second_person['name']}, a {second_person['description']}, "
                  f"from {second_person['country']}")
        else:
            ans_correct = False
            print(f"\nSorry, that's wrong.\n\n{first_person['name']} has {first_person_followers} followers\n"
                  f"{second_person['name']} has {second_person_followers} followers\n\nFinal score: {score}")


""" From Angela"""


# def get_random_account():
#     """Get data from random account"""
#     return random.choice(data)
#
#
# def format_data(account):
#     """Format account into printable format: name, description and country"""
#     name = account["name"]
#     description = account["description"]
#     country = account["country"]
#     # print(f'{name}: {account["follower_count"]}')
#     return f"{name}, a {description}, from {country}"
#
#
# def check_answer(guess, a_followers, b_followers):
#     """Checks followers against user's guess and returns True if they got it right. Or False if they got it wrong."""
#     if a_followers > b_followers:
#         return guess == "a"
#     else:
#         return guess == "b"
#
#
# def game():
#     print(logo)
#     score = 0
#     game_should_continue = True
#     account_a = get_random_account()
#     account_b = get_random_account()
#
#     while game_should_continue:
#         account_a = account_b
#         account_b = get_random_account()
#
#         while account_a == account_b:
#             account_b = get_random_account()
#
#         print(f"Compare A: {format_data(account_a)}.")
#         print(vs)
#         print(f"Against B: {format_data(account_b)}.")
#
#         guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#         a_follower_count = account_a["follower_count"]
#         b_follower_count = account_b["follower_count"]
#         is_correct = check_answer(guess, a_follower_count, b_follower_count)
#
#         os.system('cls')
#         print(logo)
#         if is_correct:
#             score += 1
#             print(f"You're right! Current score: {score}.")
#         else:
#             game_should_continue = False
#             print(f"Sorry, that's wrong. Final score: {score}")
#
#
# game()
#
# '''
#
# FAQ: Why does choice B always become choice A in every round, even when A had more followers?
#
# Suppose you just started the game, and you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (
# 174k). Instagram has more followers, so choice A is correct. However, the subsequent comparison should be between
# Selena Gomez (the new A) and someone else. The reason is that everything in our list has fewer followers than
# Instagram. If we were to keep Instagram as part of the comparison (as choice A) then Instagram would stay there for
# the rest of the game. This would be quite boring. By swapping choice B for A each round, we avoid a situation where
# the number of followers of choice A keeps going up over the course of the game. Hope that makes sense :-)
#
# '''
#
# # Generate a random account from the game data.
#
# # Format account data into printable format.
#
# # Ask user for a guess.
#
# # Check if user is correct.
# # Get follower count.
# # If Statement
#
# # Feedback.
#
# # Score Keeping.
#
# # Make game repeatable.
#
# # Make B become the next A.
#
# # Add art.
#
# # Clear screen between rounds.
