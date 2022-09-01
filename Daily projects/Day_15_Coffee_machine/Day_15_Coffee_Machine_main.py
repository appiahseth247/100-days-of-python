"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 15 - Coffee Machine                                                                               *
*    Subject:  Application                                                                                  *
*    Date: 2022-03-24                                                                                       *
*************************************************************************************************************
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def make_payment():
    """Takes the money and return the coffee and change if any"""
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    inserted_amount = float(0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies)
    if inserted_amount > MENU[want]["cost"]:
        change = round(inserted_amount - MENU[want]["cost"], 2)
        print(f"Here is ${change} in change")
    if inserted_amount >= MENU[want]["cost"]:
        global start_money, start_coffee, start_water, start_milk
        start_money += MENU[want]["cost"]
        start_water -= MENU[want]["ingredients"]["water"]  # 50
        start_coffee -= MENU[want]["ingredients"]["coffee"]  # 18
        start_milk -= MENU[want]["ingredients"]["milk"]
        print(f"Here is your {want} ☕️. Enjoy!")
    elif inserted_amount < MENU[want]["cost"]:
        print("Sorry that's not enough money. Money refunded.")


def serve_user():
    """Checks if there is enough resources to make the coffee"""
    global start_water, start_milk, start_coffee
    if want == "espresso":
        if start_water >= 50 and start_coffee >= 18:
            make_payment()
        else:
            if start_water < 50:
                print("Sorry there is not enough water.")
            if start_coffee < 18:
                print("Sorry there is not enough coffee.")

    if want == "latte":
        if start_water >= 200 and start_milk >= 150 and start_coffee >= 24:
            make_payment()
        else:
            if start_water < 200:
                print("Sorry there is not enough water.")
            if start_milk < 150:
                print("Sorry there is not enough coffee.")
            if start_coffee < 24:
                print("Sorry there is not enough coffee.")

    if want == "cappuccino":
        if start_water >= 200 and start_milk >= 150 and start_coffee >= 24:
            make_payment()
        else:
            if start_water < 250:
                print("Sorry there is not enough water.")
            if start_milk < 100:
                print("Sorry there is not enough coffee.")
            if start_coffee < 24:
                print("Sorry there is not enough coffee.")


start_water = resources["water"]
start_milk = resources["milk"]
start_coffee = resources["coffee"]
start_money = 0
machine_on = True
while machine_on:
    want = input("What would you like? (espresso/latte/cappuccino): ")
    if want == "off":
        machine_on = False
        print("Thanks for using our service")
    elif want == "report":
        print(f"Water: {start_water}ml\nMilk: {start_milk}ml\nCoffee: {start_coffee}g\nMoney: ${start_money}")
    elif want == "espresso" or "latte" or "cappuccino":
        serve_user()
