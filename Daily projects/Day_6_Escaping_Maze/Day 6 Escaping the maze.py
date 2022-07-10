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
"""
# Exercise 6.3 - Reeborg's world Hurdle 3
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
"""
