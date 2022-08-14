"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 10 - Calculator                                                                                   *
*    Subject: Function with output (return keyword)                                                         *
*    Date: 2022-03-13                                                                                       *
*************************************************************************************************************
"""
# Day 10 project - Calculator
from Day_10_Calculator_art import logo


# Add
def add(n1, n2):
    return n1 + n2


# subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))

    continue_ = True
    while continue_:
        for operation in operations:
            print(operation)
        select_operator = input("Which operator do you want? Type +, - * or /")
        num2 = float(input("What is the next number?: "))
        # if select_operator == "+":
        #   answer = add(num1, num2)
        # elif select_operator == "-":
        #   answer = subtract(num1, num2)
        # elif select_operator == "*":
        #   answer = multiply(num1, num2)
        # elif select_operator == "/":
        #   answer = divide(num1, num2)
        operation_function = operations[select_operator]
        answer = operation_function(num1, num2)
        print(f"{num1} {select_operator} {num2} = {answer}")

        next_calculation = input(
            f"Type 'y' to continue calculating with {answer} or type 'n' to exit and 'r' to reset the calculator.:")
        if next_calculation == "y":
            num1 = answer
            # select_operator = input("Which operator do you want? Type +, - * or /")
            # next_number = int(input("What is the next number?:"))
            # operation_function = operations[select_operator]
            # next_answer = int(operation_function(current_answer, next_number))
            # print(f"{current_answer} {select_operator} {next_number} = {next_answer}")
            # current_answer += next_answer
        elif next_calculation == "r":
            continue_ = False
            calculator()  # function itself to repeat the whole process (recurssion)
        elif next_calculation == "n":
            continue_ = False
            print("Thanks for using my calculator")


calculator()
