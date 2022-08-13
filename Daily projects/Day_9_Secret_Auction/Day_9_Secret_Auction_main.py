"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 9 -  Secret Auction                                                                               *
*    Subject:  Dictionaries and Nesting                                                                     *
*    Date: 2022-03-10                                                                                       *
*************************************************************************************************************
"""

# Day 9 project -  Secret Auction

# from replit import clear
import os  # This let you use clear function to clear the output
from Day_9_art import logo

print(logo)

bidders_log = {}
highest_bid = 0

bidders_left = True
while bidders_left:
    name = input("What is your name?: ")
    amount = int(input("What is your bid?: $"))
    # blind_auction(name, amount)
    if amount > highest_bid:
        highest_bid = amount
    bidders_log[name] = amount
    highest_bidder = max(bidders_log, key=lambda key: bidders_log[key])  # to find key with max value
    # highest_amount = max(bidders_log.values())
    person_left = input("Is there someone else to bid? Type 'yes' or 'no': ").lower()
    if person_left == "yes":
        # clear()
        os.system('cls')
    else:
        bidders_left = False
        os.system('cls')
        # loop through the bidder_list and print out the user with the highest bid
        print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}.")
