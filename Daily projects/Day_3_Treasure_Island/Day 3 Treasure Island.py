"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 3 - Treasure Island                                                                               *
*    Subject: conditional statements, logical operators, Code blocks and Scope                              *
*    Date: 2022-02-13                                                                                       *
*************************************************************************************************************
"""

# Exercise 3.5 - Love Calculator
'''
Instructions
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is **z**."
e.g.

name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

Example Input 1
'''
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
love1 = name1.lower()
love2 = name2.lower()
couple_name = love1 + " & " + love2
print(couple_name)
T = couple_name.count('t')
# if T == 1:
#     print(f"T occurs {T} time")
# else:
#     print(f"T occurs {T} times")

R= couple_name.count('r')
# if R == 1:
#     print(f"R occurs {R} time")
# else:
#     print(f"R occurs {R} times")

U = couple_name.count('u')
# if U == 1:
#     print(f"U occurs {U} time")
# else:
#     print(f"U occurs {U} times")

E = couple_name.count('e')
# if E == 1:
#     print(f"E occurs {E} time")
# else:
#     print(f"E occurs {E} times")

L = couple_name.count('l')
# if L == 1:
#     print(f"L occurs {L} time")
# else:
#     print(f"L occurs {L} times")

O= couple_name.count('o')
# if O == 1:
#     print(f"O occurs {O} time")
# else:
#     print(f"O occurs {O} times")

V = couple_name.count('v')
# if V == 1:
#     print(f"V occurs {V} time")
# else:
#     print(f"V occurs {V} times")

# R = couple_name.count('r')
# print(R)
# U = print(couple_name.count('u'))
# E = print(couple_name.count('e'))

# L = print(couple_name.count('l'))
# O = print(couple_name.count('o'))
# V = print(couple_name.count('v'))

# print(type(T))
true_sum = str(T+R+U+E)
#print(true_sum)

love_sum = str(L+O+V+E)
#print(love_sum)
love_score_added =  (true_sum + love_sum )
love_score = int(love_score_added)

# print(type(love_score))
# print(f"Your score is   {love_score}.")

if love_score  >=90:
    print(f"Your love score is  {love_score},  you go together like coke and mentos.")
elif love_score >=70 and love_score <=90:
    print(f"Your love score is  {love_score}, you are alright together, just make it happen!")
elif love_score >=40 and love_score <= 70:
    print(f"Your love score is  {love_score}, you are alright together.")
else:
    print(f"Your love score is {love_score}. Seems impossible in the sight of men but prayers can do it!")
