"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 6 - Escaping the Maze                                                                             *
*    Subject: Functions, While Loops, Code block                                                            *
*    Date: 2022-02-27                                                                                       *
*************************************************************************************************************
The code below will only run at Reeborg's world website. So follow the link below to run the code there.
Just copy and paste
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
"""
# Exercise 6.4 - Reeborg's world Hurdle 4
"""
def turn_right():

    turn_left()

    turn_left()

    turn_left()

while not at_goal():

    if front_is_clear():

        move()

        if right_is_clear():

            turn_right()

    else:

        turn_left()
"""
# my code below which works perfectly for most cases but not others.

"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_right()
    move()
    turn_right()
    move()

while not at_goal():
    while front_is_clear():
        move()
    if wall_in_front:
        turn_left()
    while wall_on_right():
        move()
    if right_is_clear():
        jump()
    while front_is_clear():
        move()
    if wall_in_front():
        turn_left()
"""
