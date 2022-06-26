"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 3 - Treasure Island                                                                               *
*    Subject: conditional statements, logical operators, Code blocks and Scope                              *
*    Date: 2022-02-13                                                                                       *
*************************************************************************************************************
"""

# Day 3 Project: Treasure Island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print(
    "Your mission is to find the treasure and sweetheart! She is hidden somewhere on this island. Id she is really "
    "yours, you can't miss her")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
step_one = input("You're at a crossroad. Where do you want to go? Type left or right: \n").lower()

if step_one == "left":
    step_two = input(
        "The island is in the middle of a lake now! Do you want to swim to the island to meet her or you want to wait "
        "for  a safe boat? Type swim or wait: \n").lower()
    if step_two == "swim":
        last_step = input(
            "Now your are at her house on the island but there are three door colors. Your you choose the right "
            "color, viola! type red, blue or yellow\n").lower()
        if last_step == "blue":
            print("You win! Congratulation! You may enjoy")
        elif last_step == "yellow":
            print("Game over! When did yellow become the color of love? You've been eaten by beast")
        elif last_step == "red":
            print("Game over! Don't you know that red is a sign of danger huh? You've been burned by fire")
        else:
            print("Invalid input! Game over")
    else:
        print("Game over! You attacked by a trout while swimming! Do you know what a trout is? google it")
else:
    print(" Oh dear! That was too quick an exit! You fell into a hole of vampires! Game over! You may start again")
