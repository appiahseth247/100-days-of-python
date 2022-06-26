"""
*****************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                   *
*    Author: Seth Appiah                                        *
*    Day: 2 - Tip Calculator                                    *
*    Subject: Data types, f-string                              *
*    Date: 2022-02-10                                           *
*****************************************************************
"""
# Tip Calculator
"""This code calculates the amount each person should pay on a bill"""

print("Welcome to tip calculator ?")
bill = float(input("What is the total bill?: $"))
number_of_people = int(input("How many people are to pay this bill?: "))
tip_percentage = int(input(" How much tip do you want to give, 12, 10, 15 0r 20?: "))
tip = (tip_percentage / 100 * bill)
Total_bill = bill + tip
# amount_per_head_exact = round((Total_bill/number_of_people), 2)
amount_per_head = Total_bill / number_of_people
# Final_amount = round(amount_per_head_exact, 2)
Final_amount = "{:0.2f}".format(amount_per_head)  # "{:0.2f}".format rounds the number to 2 significance figures
print(f"Each person should pay ${Final_amount}")