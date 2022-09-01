"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 16 - OOP Coffee Machine                                                                           *
*    Subject:  Intro to Object-Oriented Programing (OOP)                                                    *
*    Date: 2022-04-09                                                                                       *
*************************************************************************************************************
"""

from Day_16_OOP_menu import Menu, MenuItem
from Day_16_OOP_coffee_maker import CoffeeMaker
from Day_16_OOP_money_machine import MoneyMachine

# drink = MenuItem
# print(drink)
# money_machine = MoneyMachine()
# coffee_maker = CoffeeMaker()
# menu = Menu()
# # menu_item = MenuItem()
#
# machine_on = True
#
# while machine_on:
#     choice = input(f"What would you like? {menu.get_items()}")
#     if choice == "off":
#         machine_on = False
#     elif choice == "report":
#         coffee_maker.report()
#         money_machine.report()
#     else:
#         drink = menu.find_drink(choice)
#         if coffee_maker.is_resource_sufficient(drink):
#             if money_machine.make_payment(drink.cost):
#                 coffee_maker.make_coffee(drink)


menu = Menu()  # create menu from the Menu class
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True

while machine_on:
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
