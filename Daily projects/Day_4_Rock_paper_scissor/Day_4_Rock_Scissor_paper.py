"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 4 - Rock Paper Scissors                                                                           *
*    Subject: Randomisation and python list                                                                 *
*    Date: 2022-02-20                                                                                       *
*************************************************************************************************************
"""
# Day 4 Project- Rock Paper Scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

choices = [rock, paper, scissors]

Your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if Your_choice >= 3 or Your_choice < 0:  # To force user to type either 0, 1 or 2
    print("That is not a valid choice, you lose")
else:
    your_image = choices[Your_choice]
    Computer_choice = random.randint(0, 2)  #
    computer_image = choices[Computer_choice]

    if Your_choice == Computer_choice:
        print(f"You chose:\n {your_image}\nComputer chose:\n {computer_image}\n That's a draw  ")
    elif Your_choice == 0 and Computer_choice == 2:  # Remember index 0 is rock and 2 is scissors
        print(f"You chose:\n {your_image}\nComputer chose:\n {computer_image}\n You win ")
    elif Your_choice == 2 and Computer_choice == 0:
        print(f"You chose:\n {your_image}\nComputer chose:\n {computer_image}\n You lose ")
    elif Computer_choice > Your_choice:  # As index 3 (scissors) wins over 2(paper) and 2(paper) wins over 1(rock)
        print(f"You chose:\n {your_image}\nComputer chose:\n {computer_image}\nYou lose ")
    elif Your_choice > Computer_choice:
        print(f"You chose:\n {your_image}\nComputer chose:\n {computer_image}\n You win ")
