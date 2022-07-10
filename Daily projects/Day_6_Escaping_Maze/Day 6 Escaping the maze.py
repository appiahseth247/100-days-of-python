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
# Exercise 6.1 - Reeborg's world Hurdle 1
# Goto: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url
# =worlds%2Ftutorial_en%2Fhurdle1.json
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


for n in range(1, 13):
    if n % 2 == 0:
        jump()
    else:
        move()

#Another one by Angela
for step in range (6): # 6 because there are 6 hurdles to finishing flag point
    move()
    jump()
"""
